from job.models import State

import pycountry

for country in pycountry.countries:
    new_country = State(name=country.name)
    new_country.save()