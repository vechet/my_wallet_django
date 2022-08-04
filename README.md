## Generate requirements

```
pip freeze > requirements.txt
```

## Setup

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run

```
python manage.py runserver
uvicorn my_wallet_django.main:app --reload
```

##

```
python manage.py startapp members
python manage.py makemigrations xxxxx
python manage.py migrate
```

## Is it possible to generate django models from the database?

```
python manage.py inspectdb
```

## Save this as a file by using standard Unix output redirection:

```
python manage.py inspectdb > generate_models.py
```
