# dohodathi's FlaskFactoryBone - Small

also available in the future, the versions medium and large!

## Purpose

e.g. for creating a rapid app with a db but without user authentication

### does not deliver

for this features look for medium and large versions in the future

* user authentication

* templates

* extensionibility

## Installation

### Requirements

We still use python2 with a postgres database. We recommend using a virtual environment.


### get this

* clone this repository: `git clone https://github.com/danielthiel/FlaskFactoryBone-Small.git`

* go to the directory: `cd FlaskFactoryBone-Small/`

* create the virtual environment: `virtualenv venv`

* enter the environment: `source venv/bin/activate`

* install all python packages only for the environment: `pip install -r requirements.txt`

## Usage

* run with: `python manage.py runserver`

### Database

* create a new postgres user: `sudo -u postgres createuser -s -P dohodathi`

* in the config the password `password` is used, change the config with your used (also if you create a different user)

* create a db: `createdb -U dohodathi -h localhost flaskbone`

* reset the database: `python manage.py db_reset`

### Test it on localhost

* again run with: `python manage.py runserver`

* then (on a different terminal) run: `curl http://localhost:5000/api/v1/friends`

* should return an empty list

### Heroku

This app is build to run well on heroku. Take this steps to deploy on heroku.

* new heroku app: `heroku apps:create --region eu` or existing one `git remote add heroku git@heroku.com:YOUR-HEROKU-PROJECT.git`

* set config so the heroku config class will be used: `heroku config:set FLASK_CONFIG=heroku`

* add a postgres database to the project: `heroku addons:add heroku-postgresql`

* retrieve the databse infos `heroku pg:info` and write the data in the config file (heroku class)

* reset the database: `foreman run python manage.py db_reset` (foreman will use the environment in the `.env` file - so it resets the heroku db)

* deploy your repository to heroku: `git push heroku master`

* now your heroku server should run, look into the logs: `heroku logs`

### Migration

Migration via Flask-Migration (using Alembic) changes your database when you change your model without resetting the database.
To use it, you need to initialze migration:

* `python manage.py db init`

Created files (in the `migrations` dir need to be added under version control! After that every change in your models can be commited for migration:

* `python manage.py db migrate -m "message"`

This will create a change request for your database. To apply these changes run:

* `python manage.py db upgrade`

If you are using heroku commit everything, then run your upgrade via foreman:

* `foreman run python manage.py db upgrade`

and your heroku database is also up to date.

## Enviroment

Some enviorment variables that are used by this Bone. Every one should be optional.

* `FLASK_CONFIG` look in the config file for all available configurations

* `FLASK_LOG_FILE` destination for default logging - not used on heroku configuration
