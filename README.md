# Система Тестування

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

Це приклад проекту для ілюстрації реалізації декількох типів користувачів. У цьому додатку Django вчителі можуть створювати тести, а учні можуть їх виконувати.

![Система Тестування Screenshot](/teacher-quiz.png)


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/ajax3101/quize.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


