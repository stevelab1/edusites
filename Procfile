web: gunicorn edusites.wsgi --log-file -
web2: daphne chat.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2