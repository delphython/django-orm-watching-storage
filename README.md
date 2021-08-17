# Bank's security console

Bank's security console is a website that can be connected to a remote database with visits and pass cards of bank employees.

## Prerequisites

Use `pip` to install dependences:
```bash
python -m pip install -r requirements.txt
```
## Installation
You have to set environment variables for regional settings and database connection.

Create `.env` file in project directory. Copy this text in it:
```
export DB_ENGINE=""
export DB_HOST=""
export DB_PORT=""
export DB_NAME=""
export DB_USER=""
export DB_PASSWORD=""
export SECRET_KEY=""
export LANGUAGE_CODE=""
export TIME_ZONE=""
export LOG_LEVEL=False
```
`DB_ENGINE` variable set database backend to use. The built-in database backends are:
`django.db.backends.postgresql`
`django.db.backends.mysql`
`django.db.backends.sqlite3`
`django.db.backends.oracle`

`DB_HOST` variable set host to use when connecting to the database. An empty string means localhost.

`DB_PORT` variable set the port to use when connecting to the database. An empty string means the default port.

`DB_NAME` variable set name of the database to use.

`DB_USER` variable set the username to use when connecting to the database.

`DB_PASSWORD` variable set the password to use when connecting to the database.

`SECRET_KEY` variable set the secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

`LANGUAGE_CODE` variable set the language code for this installation. This should be in standard [language ID format](https://docs.djangoproject.com/en/3.2/topics/i18n/#term-language-code).

`TIME_ZONE` variable set the time zone for this database connection or None.

`LOG_LEVEL` variable set the boolean that turns on/off debug mode. Default: `False`.

## Usage example

How to start local web server:
```sh
python manage.py runserver 0.0.0.0:8000
```

Open link [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to use Bank's security console.

## Meta

Vitaly Klyukin – [@delphython](https://t.me/delphython) – [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
