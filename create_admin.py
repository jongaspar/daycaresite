#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'jongaspar@gmail.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'DayCare2026SecureAdmin')

user, created = User.objects.get_or_create(
    username=username,
    defaults={'email': email, 'is_staff': True, 'is_superuser': True}
)
user.set_password(password)
user.save()

if created:
    print(f'Admin user "{username}" created.')
else:
    print(f'Admin user "{username}" password updated.')
