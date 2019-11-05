# CFProject

username: admin
password: pass

1. Need one endpoint called loanapp/ to take application. Should be able to consume this json.

Used Postman to ingest json in the body
localhost:8000/loanapp/


2. Need one endpoint called status/ to provide a status on an application submitted given a loanapp id. Be creative about the status to return.
localhost:8000/status/?id={loanapp id}

(List of cmds)

run the project: python manage.py runserver

python manage.py makemigrations

python manage.py migrate

python manage.py test loan.tests

