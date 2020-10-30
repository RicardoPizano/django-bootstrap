# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from rest_framework.views import APIView

from users.models import User
from helpers import get_client_ip
from helpers.jwt import create_token
from helpers.responses import success, bad_request, no_found, unauthorized


class Login(APIView):

    @staticmethod
    def post(request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email)
            if user.is_active or user.deleted_at is None:
                user = authenticate(username=email, password=password)
                if user:
                    ip = get_client_ip(request)
                    token = create_token(user, ip)
                    response = {
                        'email': user.email,
                        'role': user.role,
                        'role_name': user.get_role_display(),
                        'full_name': user.get_full_name(),
                        'token': token
                    }
                    return success(response)
                else:
                    return unauthorized({'message': 'Usuario o contraseña incorrectos'})
            else:
                return unauthorized({'message': 'Lo sentimos, tu cuenta ha sido deabilitada o eliminada, '
                                                'contacte a soporte'})
        except User.DoesNotExist:
            return no_found({'message': 'Usuario o contraseña incorrectos'})
        except KeyError:
            return bad_request({})
