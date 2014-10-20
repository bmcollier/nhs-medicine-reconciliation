from django.db import models
from django.core.validators import RegexValidator

from medicine.models import VirtualMedicinalProduct

import time

def generate_hospital_id():
    return str(int(time.time() * 10))

class Patient(models.Model):
    hospital_id = models.CharField(max_length=100, default=generate_hospital_id, unique=True, editable=False)
    nhs_number = models.CharField(max_length=12, validators=[RegexValidator(regex=r'[0-9]{3} [0-9]{3} [0-9]{4}', message='NHS Number must be in the format 000 000 0000')])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.nhs_number)

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

class PatientMedication(models.Model):
    SOURCE_CHOICES = (
        ('RELATIVE', 'Relative of Patient'),
        ('CARER', 'Carer of Patient'),
        ('PATIENT', 'Patient'),
        ('MEDICINE_BAG', 'Medicine Bag'),
        )

    patient = models.ForeignKey(Patient, blank=True, null=True)
    virtual_medicinal_product = models.ForeignKey(VirtualMedicinalProduct, null=True)
    form = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)
    dose = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    special_instructions = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    reason = models.CharField(max_length=1000, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.patient.get_full_name(), self.virtual_medicinal_product_pack.nm)