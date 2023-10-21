from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'Portland.json'
def load_data(nearbyshops, schema_editor):
    Portland = nearbyshops.get_model('PortlandModel', 'Portland')
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
                    p=Portland()
                    p.address = address
                    p.city = city
                    p.name = name
                    p.location = location
                    p.save()
            except KeyError:
                print('false') 
                pass 


class Migration(migrations.Migration):

    dependencies = [
        ('PortlandModel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
