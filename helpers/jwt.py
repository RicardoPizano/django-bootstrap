# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

import jwt

from bootstrap import constants
from users.models import Token


def create_token(user, ip):
    payload = {
        'id': user.pk,
        'email': user.email,
        'role': user.role,
        'exp': (datetime.now() + timedelta(days=30)).timestamp()
    }
    token = jwt.encode(payload, constants.jwt_key, algorithm='HS256')
    Token.objects.create(user=user, token=token.decode("utf-8"), ip=ip)
    return token.decode("utf-8")


def validate_token(token):
    try:
        try:
            save_token = Token.objects.get(token=token)
            payload = jwt.decode(token, constants.jwt_key, algorithm='HS256')
            if save_token.user.pk is payload['id'] and save_token.user.email == payload['email'] \
                    and save_token.deleted_at is None:
                return True, payload
            else:
                return False, {}
        except Token.DoesNotExist:
            return False, {}
    except jwt.InvalidSignatureError:
        return False, {}
    except jwt.ExpiredSignatureError:
        return False, {'expired': True}


def delete_token(token, user):
    try:
        token = Token.objects.get(user=user, token=token)
        token.deleted_at = datetime.now()
        token.save()
        return True, ""
    except Token.DoesNotExist:
        return False, "el token no existe"
