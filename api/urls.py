# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from api.views import Login

urlpatterns = [
    path('login', Login.as_view(), name='api_login'),
]
