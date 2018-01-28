from pyramid_celery import celery_app as app


@app.task
def print_to_stdout():
    print('A simple task from celery')
