from patient.models import *
from django.core.management.base import BaseCommand






class Command(BaseCommand):
    help = 'Do some hocus pocus.'
    
    def handle(self, *args, **options):
        dai_id = 15
        nash_id = 20

        dai = Patient.objects.get(id=dai_id)
        nash = Patient.objects.get(id=nash_id)

        gp_meds = PatientMedication.objects.filter(patient=dai)

        for p in Patient.objects.all().exclude(id=dai_id):
            for med in gp_meds:
                gp = GPMedication()
                gp.patient = p
                gp.virtual_medicinal_product = med.virtual_medicinal_product
                gp.form = med.form
                gp.strength = med.strength
                gp.route = med.route
                gp.dose = med.dose
                gp.frequency = med.frequency
                gp.duration = med.duration
                gp.special_instructions = med.special_instructions
                gp.reason = med.reason
                gp.comments = med.comments
                gp.status = med.status

                gp.save()

        PatientMedication.objects.filter(patient=dai).delete()

        patient_meds = PatientMedication.objects.filter(patient=nash)

        for p in Patient.objects.all().exclude(id=nash_id):
            for med in patient_meds:
                pm = PatientMedication()
                pm.patient = p
                pm.virtual_medicinal_product = med.virtual_medicinal_product
                pm.form = med.form
                pm.strength = med.strength
                pm.route = med.route
                pm.dose = med.dose
                pm.frequency = med.frequency
                pm.duration = med.duration
                pm.special_instructions = med.special_instructions
                pm.reason = med.reason
                pm.comments = med.comments
                pm.status = med.status
                pm.source = med.source
                pm.last_taken = med.last_taken

                pm.save()