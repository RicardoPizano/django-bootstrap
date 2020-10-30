# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response


def success(data):
    return Response(data=data, status=status.HTTP_200_OK)


def no_content():
    return Response(data={}, status=status.HTTP_204_NO_CONTENT)


def bad_request(data):
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def no_found(data):
    return Response(data=data, status=status.HTTP_404_NOT_FOUND)


def unauthorized(data):
    return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)


def conflict(data):
    return Response(data=data, status=status.HTTP_409_CONFLICT)
