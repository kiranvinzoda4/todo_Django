import jwt, datetime
from django.http import HttpResponse
from .models import user
from django.contrib.auth.hashers import make_password, check_password


def get_password_hash(password):
        return make_password(password)

def verify_password(plain_password, hashed_password):
    return check_password(plain_password, hashed_password)


def encode_token(user_id):
    payload = {
        "id" : user_id,
        "exp":datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        "iat":datetime.datetime.utcnow()
    }
    token = jwt.encode(payload,'secret', algorithm='HS256')
    return token


def decode_token(token):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            return payload['id']
        except jwt.ExpiredSignatureError:
            raise HttpResponse(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HttpResponse(status_code=401, detail='Invalid token')


def user_varification(token):
    result_id = decode_token(token)
    user_record = user.objects.get(id = result_id)
    if user_record is not None:
        return True
    else:
        return False