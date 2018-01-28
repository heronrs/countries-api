"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.include("pyramid_celery")
    config.configure_celery("countriesapi.ini")
    config.scan()
    return config.make_wsgi_app()
