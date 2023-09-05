"""
WSGI config for ci_fsd_pp4_the_wc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ci_fsd_pp4_the_wc.settings')

application = get_wsgi_application()
