# Procfile

release: python manage.py db upgrade
web: gunicorn wsgi:application