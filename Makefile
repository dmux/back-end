
PROJECT=backend

migrate:
	python manage.py makemigrations
	python manage.py migrate

data_development:
	python manage.py dumpdata --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission  > fixtures/development.json
	bzip2 -f fixtures/development.json

load_data_development:
	python manage.py loaddata fixtures/development.json.bz2

run:
	python manage.py runserver 127.0.0.1:8000

check:
	poetry run pycodestyle --exclude=*/static/*,*/migrations/*,*/templates/*,.venv/* .
	poetry run yapf -i -vv -e */static/* -e */migrations/* -e */templates/* -e *.venv/* --recursive .
	poetry run bandit -x *.venv/* -r .

api_test_jwt:
	curl -d '{"username": "admin","password": "DesafioHyperativa"}' \
     -H "Content-Type: application/json" \
     -X POST http://127.0.0.1:8000/api/token/

api_test_upload:
	curl -F "post=@contrib/DESAFIO-HYPERATIVA.txt" \
     -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODUwNDM0LCJqdGkiOiIyNDhhZTc0ZTc4Yzk0MTJhOTk3MjcwYTRlNmQwYmIyMyIsInVzZXJfaWQiOjF9.fNpOZuCROeQ94hHoLjdvNH0hI7y8WccUM0Amo-NPGE0" \
     -X POST http://127.0.0.1:8000/api/app/card/upload

api_test_search:
	curl -X GET "http://localhost:8000/api/app/card/search/456897912999999" \
	-H  "accept: application/json" \
	-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODUwNDM0LCJqdGkiOiIyNDhhZTc0ZTc4Yzk0MTJhOTk3MjcwYTRlNmQwYmIyMyIsInVzZXJfaWQiOjF9.fNpOZuCROeQ94hHoLjdvNH0hI7y8WccUM0Amo-NPGE0"
