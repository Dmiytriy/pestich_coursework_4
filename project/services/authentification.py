import base64
import calendar
import datetime
import hashlib
import hmac
from flask import abort
import jwt

from project.setup_db import db

from project.constant import SECRET, ALGO, PWD_HASH_SALT, PWD_HASH_ITERATIONS
from project.container import user_service


def generate_tokens(email, password, is_refresh=False):
    user = user_service.get_user_by_email(email)

    if user is None:
        raise abort(404)

    if not is_refresh:
        db_pass = user.password
        if not check_password(db_pass, password):
            raise abort(400)

    data = {
        'user_id': user.id,
        'user_email': user.email
           }
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data['exp'] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, SECRET, algorithm=ALGO)

    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data['exp'] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

    return {'access_token': access_token,
            'refresh_token': refresh_token}


def check_password(db_hash, client_password):

    decoded_digest = base64.b64decode(db_hash)

    hash_digest = hashlib.pbkdf2_hmac(
        'sha256',
        client_password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )

    return hmac.compare_digest(decoded_digest, hash_digest)


def examination_refresh_token(refresh_token):
    try:
        data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])

    except Exception as e:
        return f'{e}', 401

    email = data.get('user_email')

    return generate_tokens(email, None, is_refresh=True)


def get_email_from_header(header: str):

    token = header.split('Bearer ')[-1]
    data_dict = jwt.decode(token, SECRET, ALGO)

    email = data_dict.get('user_email')

    return email


def change_the_password(user_email, pass1, pass2):

    user = user_service.get_by_email(user_email)

    db_pass = user.password

    is_confirmed = check_password(db_pass, pass1)

    if is_confirmed:

        user.password = user_service.get_hash(pass2)

        db.session.add(user)
        db.session.commit()

        return '', 204

    abort(401)

