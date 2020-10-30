# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import BasePermission

from bootstrap.enums import Roles
from helpers.jwt import validate_token
from helpers.responses import bad_request, unauthorized


class RoleAdministratorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.META.get('HTTP_AUTH'):
            token_correct, payload = validate_token(request.META.get('HTTP_AUTH'))
            if token_correct:
                if payload['role'] is Roles.Admin:
                    request.data['payload'] = payload
                    return request and True
                else:
                    return request and False
            else:
                return request and False
        else:
            return request and False


class RoleClientPermission(BasePermission):

    def has_permission(self, request, view):
        if request.META.get('HTTP_AUTH'):
            token_correct, payload = validate_token(request.META.get('HTTP_AUTH'))
            if token_correct:
                if payload['role'] is Roles.Client:
                    request.data['payload'] = payload
                    return request and True
                else:
                    return unauthorized({}) and False
            else:
                return bad_request({}) and False
        else:
            return bad_request({}) and False


class AllRolesPermission(BasePermission):

    def has_permission(self, request, view):
        if request.META.get('HTTP_AUTH'):
            token_correct, payload = validate_token(request.META.get('HTTP_AUTH'))
            if token_correct:
                request.data['payload'] = payload
                return request and True
            else:
                if payload.get('expired'):
                    return unauthorized({'message': 'session expired'})
                return unauthorized({'message': 'bad authentication'}) and False
        else:
            return unauthorized({'message': 'token was expected'}) and False


class PostMethod(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False


class GetMethod(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return False


class PutMethod(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'PUT':
            return True
        else:
            return False


class DeleteMethod(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return True
        else:
            return False
