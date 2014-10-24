from patient.models import *
from django.core.management.base import BaseCommand

from time import sleep
class Command(BaseCommand):
    help = 'Populates random data for demonstration purposes.'
    
    def handle(self, *args, **options):
        for i in range(0, 100):
            gp = GeneralPractitioner()
            gp.save()

        for i in range(0, 20):
            p = Patient()
            p.save()
            sleep(1)