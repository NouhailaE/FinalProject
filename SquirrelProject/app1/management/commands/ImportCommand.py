
from django.utils import timezone
from Sightings.models import squirrel

from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], encoding = 'utf-8') as fp:
            reader = csv.DictReader(fp)
            data = list(reader) 
        
        sightings = []

        for dict_ in data:

            sightings.append(squirrel(
                Y  = float(dict_['Y']),
                X  = float(dict_['X']),
                UniqueID = dict_['Unique Squirrel ID'],
                Shift = dict_['Shift'].lower,
                Date = timezone.datetime.strptime(dict_['Date'],'%m%d%Y').date(),
                Age = dict_['Age'],
                Fur = dict_['Primary Fur Color'],
                Location = dict_['Location'],
                Spec_location = dict_['Specific Location'],
                Running = dict_['Running'].lower()=='true', 
                Chasing = dict_['Chasing'].lower()=='true',
                Climbing = dict_['Climbing'].lower() == 'true',
                Eating = dict_['Eating'].lower == 'true',
                Foraging = dict_['Foraging'].lower() == 'true',
                Other_activities = dict_['Other Activities'],
                Kuks = dict_['Kuks'].lower() == 'true',
                Quaas = dict_['Quaas'].lower() ==  'true',
                Moans = dict_['Moans'].lower() == 'true',
                Tail_Flags = dict_['Tail flags'].lower() == 'true',
                Tail_Twitches = dict_['Tail twitches'].lower() == 'true',
                Approaches = dict_['Approaches'].lower() == 'true',
                Indifferent = dict_['Indifferent'].lower() == 'true',
                Runs_From = dict_['Runs from'].lower() == 'true',
                ))



            
        squirrel.objects.all().delete()
        squirrel.objects.bulk_create(sightings)


