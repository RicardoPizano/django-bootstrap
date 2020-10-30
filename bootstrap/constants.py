# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decouple import config

created_at_field_text = 'fecha de creación'
deleted_at_field_text = 'fecha de eliminación'

jwt_key = config('JWT_KEY')
