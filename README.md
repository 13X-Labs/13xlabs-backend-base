# 13XLabs

"13xlabs-backend-base" refers to the foundational codebase used by the 13xlabs team for their backend operations. This codebase provides a starting point for building web applications and services, including authentication, database connections, and API endpoints. It is designed to be scalable and easily customizable for different projects.

## Install

### Create Virtual Environment
```bash
$ python3 -m venv venv
```

### Active Virtual Environment
```bash
$ venv/Scripts/activate (Windows)
$ source venv/bin/activate (Linux)
```

### Requirements
```bash
$ pip install -r requirements.txt
```

### Run
```bash
$ python manage.py runserver
```

## Development

### Freeze Requirements
```bash
$ pip freeze > requirements.txt
```

### Create Superuser
```bash
$ python manage.py createsuperuser
```

### Migrations
```bash
$ python manage.py makemigrations --name <migration_name> <app_name>
$ python manage.py migrate
```

