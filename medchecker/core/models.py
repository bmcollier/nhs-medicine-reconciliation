from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

import uuid

def make_uuid():
  return str(uuid.uuid4())

class NfcUser(AbstractUser):
    nfc_login_id = models.CharField(max_length=36, default=make_uuid, editable=False, unique=True, db_index=True)
    nfc_login_pin = models.IntegerField(max_length=4, default=1111)
    role = models.CharField(max_length=50, blank=True, null=True)
    nhs_trust = models.CharField(max_length=255, blank=False, null=True)

    def nfc_url(self):
        return mark_safe(u'http://us-pc:8000/unlock/%s/') % (self.nfc_login_id)