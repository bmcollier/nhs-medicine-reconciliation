from django.db import models
from django.core.validators import RegexValidator

import time

def generate_hospital_id():
    return str(int(time.time() * 10))

class Patient(models.Model):
    hospital_id = models.CharField(max_length=100, default=generate_hospital_id(), unique=True, editable=False)
    nhs_number = models.CharField(max_length=12, validators=[RegexValidator(regex=r'[0-9]{3} [0-9]{3} [0-9]{4}', message='NHS Number must be in the format 000 000 0000')])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.nhs_number)