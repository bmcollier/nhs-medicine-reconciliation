from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

def make_uuid():
  return str(uuid.uuid4())

class NfcUser(AbstractUser):
    nfc_login_id = models.CharField(max_length=36, default=make_uuid, editable=False, unique=True, db_index=True)