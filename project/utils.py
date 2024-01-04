from celery import Celery, Task
from flask import Flask 
from __appsignal__ import appsignal
from celery.signals import worker_process_init

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)
            
    @worker_process_init.connect(weak=False)
    def init_celery_tracing(*args, **kwargs):
        print("STARTING APP SIGNAL IN CELERY!")
        appsignal.start()

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app