start-backend:
	docker-compose exec django sh -c "pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080"
