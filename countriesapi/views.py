""" Cornice services.
"""
from cornice import Service

COUNTRIES = {
    'br': 'Brazil',
    'ca': 'Canada',
    'cl': 'Chile',
    'fr': 'France',
    'in': 'India',
    'it': 'Italy'
}

countries = Service(
    name='countries', path='/countries/{code}', description="Get the country!")


@countries.get()
def get_info(request):
    """Returns all countries and their 2 letter code"""
    country_code = request.matchdict['code']
    return COUNTRIES.get(country_code, 0) or COUNTRIES
