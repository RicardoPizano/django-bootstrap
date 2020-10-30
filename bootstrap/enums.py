# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djchoices import DjangoChoices, ChoiceItem


class Roles(DjangoChoices):
    Admin = ChoiceItem(1, 'Administrator')
    Client = ChoiceItem(2, "Client")
