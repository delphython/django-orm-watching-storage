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
DEBUG=False
SECRET_KEY=""
ALLOWED_HOSTS=
DATABASE_URL="postgres://user:password@host:port/db_name"

LANGUAGE_CODE="ru-ru"
TIME_ZONE="Europe/Moscow"
LOG_LEVEL=True
```

`DEBUG` variable set the boolean that turns on/off debug mode. Default: `False`.

`SECRET_KEY` variable set the secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

`ALLOWED_HOSTS` is a comma separated list of strings representing the host/domain names that this Django site can serve.  E.g. `localhost`.

`DATABASE_URL` URL string to connect to the database.
 1. `user` - variable set the username to use when connecting to the database.
 2. `password` - variable set the password to use when connecting to the database.
 3. `host` - variable set host to use when connecting to the database. An empty string means localhost.
 4. `port` - variable set the port to use when connecting to the database. An empty string means the default port.
 5. `db_name` - variable set name of the database to use.

`LANGUAGE_CODE` variable set the language code for this installation. This should be in standard [language ID format](https://docs.djangoproject.com/en/3.2/topics/i18n/#term-language-code).

`TIME_ZONE` variable set the time zone for this database connection or None.





## Usage example

How to start local web server:
```sh
python manage.py runserver 0.0.0.0:8000
```

Open link [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to use Bank's security console.

## Meta

Vitaly Klyukin – [@delphython](https://t.me/delphython) – [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
