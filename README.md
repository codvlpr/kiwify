# Kiwify API Powered by Django

## To setup the repo in development
- `$ docker-compose up -d --build`
- `$ docker exec -ti kiwify-backend python manage.py migrate`
- `$ docker exec -ti kiwify-backend python manage.py loaddata kiwify/fixtures/quiz.json`

Server is up on `http://localhost:8000`