from django.conf import settings

MY_SETTING = getattr(settings, 'EMAIL_HOST_USER', '')