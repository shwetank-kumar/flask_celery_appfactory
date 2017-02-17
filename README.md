# flask_celery_appfactory
A design pattern for working with Flask and Celery using Appfactories. To run locally:  
$ pip install -r requirements.txt  
$ redis-server  
$ celery worker -A celery_worker.celery --loglevel=info  
$ python manage.py runserver  
