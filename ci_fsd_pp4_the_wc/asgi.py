"""
ASGI config for ci_fsd_pp4_the_wc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ci_fsd_pp4_the_wc.settings')

application = get_asgi_application()
