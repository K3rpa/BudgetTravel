from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'AustinTX_tourism.json'
def load_data(nearbyshops, schema_editor):
    Austin = nearbyshops.get_model('AustinModel', 'Austin')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','N/A')
                    street = tags.get('addr:street', 'N/A')
                    city = tags.get('addr:city', 'N/A')
                    postalcode = tags.get('addr:postcode', 'N/A')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    # location = "Point( "+longitude+")"+latitude 
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    address = street + ", " + postalcode
                    a=Austin()
                    a.address = address
                    a.city = city
                    a.name = name
                    a.location = location
                    a.save()
            except KeyError:
                print('false') 
                pass 


class Migration(migrations.Migration):

    dependencies = [
        ('AustinModel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
