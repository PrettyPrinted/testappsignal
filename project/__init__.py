# from __appsignal__ import appsignal
    
# appsignal.start()

from flask import Flask 
from .utils import celery_init_app
from .tasks import add_togethers



def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            #broker_url="redis://localhost",
            #result_backend="redis://localhost",
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            #task_ignore_result=True,
        ),
    )
    celery_app = celery_init_app(app)

    @app.route("/error")
    def index():
        raise ValueError("oops")
    
    @app.route('/add')
    def addstuff():
        add_togethers.delay(1, 2)
        return "done"
    
    from time import sleep
    
    @app.route("/success")
    def index2():
        sleep(19)
        return "success"

    return app