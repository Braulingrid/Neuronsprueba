# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Braulio Zarate - Neurons Latam Inc
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
