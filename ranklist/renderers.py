# -*- coding: utf-8 -*-
from rest_framework import renderers


class UTF8JSONRenderer(renderers.JSONRenderer):
    charset = 'utf-8'