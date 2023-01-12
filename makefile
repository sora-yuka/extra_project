m:
	./manage.py makemigrations
	./manage.py migrate
u:
	./manage.py createsuperuser
r:
	./manage.py runserver
ta:
	./manage.py test account
tp:
	./manage.py test product