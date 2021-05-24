run-backend:
	docker-compose exec django sh -c "pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080"

migration-migrate:
	docker-compose exec django sh -c "python manage.py makemigrations && python manage.py migrate"


init-db:
	docker-compose exec django python manage.py init_db
