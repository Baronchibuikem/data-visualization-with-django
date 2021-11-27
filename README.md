# MyVisuals

## Readme Notes

- If the command line starts with $, the command should run with user privileges
- If the command line starts with #, the command should run with root privileges

## Retrieve code

- `$ git clone https://github.com/Baronchibuikem/data-visualization-with-django`

## Installation

- You can run this project using either docker or your localhost

### Let's configure the virtual environment for running the project locally on your localhost

- `$ python3.9 -m venv path_to_venv`
- `$ source path_to_venv/bin/activate`

### With our virtualenv setup and activated we can go ahead and run install our packages

- `$ pip install -r requirements.txt`

### We also use tailwind-css for our styling so go ahead and set it up by running

<!--
- `$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.37.2/install.sh | bash && chmod +x $HOME/.nvm/nvm.sh`
- `$ nvm install v10.23.2`
- `$ npm install`

## Running

- `$ npm run dev`
- `$ cd src`
- `$ python manage.py runserver`

### If missing migrations

- `$ python manage.py makemigrations`
- `$ python manage.py migrate`

## Testing

- `$ ./scripts/test_local_backend.sh`

## Static analysis

- `$ ./scripts/static_validate_backend.sh`

### To run black

- `$ black --skip-string-normalization --line-length=120 src`
- `$ black --skip-string-normalization --line-length=120 tests`

### To run isort

- `$ isort --atomic --profile black src`
- `$ isort --atomic --profile black tests`

### To run mypy we need to run it inside the src folder

- `$ cd src/ `
- `$ mypy .`

[install python 3.9]: https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/

## Notes

- When creating a credit officer in the call center, we must create a CallCenterCreditOfficer linking the call center's
  officer ID to our officer User. -->

## Getting Started

    git clone https://github.com/Baronchibuikem/mydjangosetup
    pip install -r requirement.txt
    cd src
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

## To run the project with docker

    docker-compose exec db psql --username=djangosetup --dbname=djangosetup_dev
    docker-compose up -d --build
    docker-compose down -v
    docker-compose -logs -f
    docker volume inspect djdocker_postgres_data
    docker-compose run db bash

## for those getting permission when trying to run the script

    cd scripts
    chmod +x the_file_name_you_want_to_run

## Testing

- `$ ./scripts/run_testcases.sh`

### To run black

- `$ ./scripts/run_blank.sh`

### To run mypy

- `$ ./scripts/run_mypy.sh`

### To run prospector

- `$ ./scripts/run_prospector.sh`

## You can run all the above script using the command below

Before you push your code after running all the inidvidual scripts, I recommend you run this script to be sure everything is covered

- `$ ./scripts/validate_backend_code.sh`
