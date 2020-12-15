web: gunicorn IE104_SC.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate