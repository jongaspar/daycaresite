#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.filter(username='admin').first(); u.set_password('DayCare2026SecureAdmin') if u else None; u.save() if u else None" || true
