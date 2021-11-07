# django-knuckle-snapper-api

An API written in Django as a knuckle-snapping exercise.

## Installation

1. Create and activate the virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

*Note: Dev dependencies can be installed optionally:*
```bash
pip install -r requirements-dev.txt
```

3. Run the migrations:
```bash
./manage.py migrate
```

4. Run the Django server:
```bash
./manage.py runserver
```

## Formatting

Run the following while within the virtual environment shell:
```bash
black ./
```
