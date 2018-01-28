Pyramid-Cornice API
===================


Simple Pyramid-Cornice API example with Celery integration.

Setup
=====
.. code-block:: shell

    pip install -r requirements.txt
    pserve countriesapi.ini
    celery worker -A pyramid_celery --ini countriesapi.ini
