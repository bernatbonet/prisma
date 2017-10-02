
django-admin startproject 
django-admin startapp

python manage.py makemigrations --settings=prisma.settings.local
python manage.py migrate --settings=prisma.settings.local

python manage.py runserver 0.0.0.0:8080 --settings=prisma.settings.local


https://github.com/bernatbonet/eclock_erp/blob/v_0.0.0.0/people/models.py