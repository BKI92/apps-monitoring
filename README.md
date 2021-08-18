# apps-monitoring
Service for monitoring the status of connected applications
# Getting started
- Download python version 3.8 and higher and activate the virtual env
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- python manage.py runapscheduler

# Description
apps-monitoring, implies that there are apps with their id in database.
For practical testing fill the table apps_app with app - objects, consider of app_id.
This operation you may execute with using Django admin panel.
In apps/management/commands/runapscheduler.py you can change the time after which the application will be considered crashed.
