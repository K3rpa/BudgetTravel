from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

# DATA_FILENAME = 'ManhattanNYC_tourism.json'
def helper(nearbyshops,filename):
    model = nearbyshops.get_model('tourism', 'Tourism')
    jsonfile = Path(__file__).parents[2] / filename

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    state = tags.get('addr:state','N/A')
                    name = tags.get('name','N/A')
                    street = tags.get('addr:street', 'N/A')
                    city = tags.get('addr:city', 'N/A')
                    postalcode = tags.get('addr:postcode', 'N/A')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    address = street + ", " +city+", "+state+","+postalcode
                    if(name != 'N/A' and state != 'N/A'):
                        m=model()
                        m.address = address
                        m.city = city
                        m.name = name
                        m.location = location
                        m.state = state
                        m.save()
            except KeyError:
                print('false') 
                pass 

def load_data(nearbyshops, schema_editor):
    helper(nearbyshops,'AustinTX_tourism.json')
    helper(nearbyshops, 'Chicago_tourism.json')
    helper(nearbyshops, 'ManhattanNYC_tourism.json')
    helper(nearbyshops, 'Portland_tourism.json')

    


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
