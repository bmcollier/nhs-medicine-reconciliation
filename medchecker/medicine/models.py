from django.db import models

class VirtualTherapeuticMoiety(models.Model):
    vtmid = models.IntegerField(primary_key=True)
    invalid = models.IntegerField(null=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, max_length=255)
    vtmidprev = models.CharField(null=True, max_length=255)
    vtmiddt = models.DateField(null=True)

    def __unicode__(self):
        return u'[VTM] %s' % self.nm

class VirtualMedicinalProduct(models.Model):
    vpid = models.IntegerField(primary_key=True)
    vpiddt = models.DateField(null=True)
    vpidprev = models.IntegerField(null=True)
    vtmid = models.ForeignKey('VirtualTherapeuticMoiety', db_column='vtmid')
    invalid = models.IntegerField(null=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, max_length=255)
    basiscd = models.IntegerField()
    nmdt = models.DateField(null=True)
    nmprev = models.CharField(null=True, max_length=255)
    basis_prevcd = models.IntegerField(null=True)
    nmchangecd = models.IntegerField(null=True) 
    combprodcd = models.IntegerField(null=True)
    pres_statcd = models.IntegerField()
    sug_f = models.IntegerField(null=True)
    glu_f = models.IntegerField(null=True)
    pres_f = models.IntegerField(null=True)
    cfc_f = models.IntegerField(null=True)
    non_availcd = models.IntegerField(null=True)
    non_availdt = models.DateField(null=True)
    df_indcd = models.IntegerField(null=True) 
    udfs = models.DecimalField(null=True, max_digits=8, decimal_places=3)
    udfs_uomcd = models.IntegerField(null=True)
    unit_dose_uomcd = models.IntegerField(null=True)

    def __unicode__(self):
        return u'[AMP] %s' % self.nm

class VirtualMedicinalProductPack(models.Model):
    vppid = models.IntegerField(primary_key=True)
    invalid = models.IntegerField(null=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, max_length=255)
    vpid = models.ForeignKey('VirtualMedicinalProduct', db_column='vpid')
    qtyval = models.DecimalField(max_digits=7, decimal_places=2)
    qty_uomcd = models.IntegerField()
    combpackcd = models.IntegerField(null=True)

    def __unicode__(self):
        return u'[VMPP] %s' % self.nm

class ActualMedicinalProduct(models.Model):
    apid = models.IntegerField(primary_key=True)
    invalid = models.IntegerField(null=True)
    vpid = models.ForeignKey('VirtualMedicinalProduct', db_column='vpid')
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(max_length=255, null=True)
    desc = models.CharField(max_length=255)
    nmdt = models.DateField(null=True)
    nm_prev = models.CharField(max_length=255, null=True)
    suppcd = models.IntegerField()
    lic_authcd = models.IntegerField()
    lic_auth_prevcd = models.IntegerField(null=True)
    lic_authchangecd = models.IntegerField(null=True)
    lic_authchangedt = models.DateField(null=True)
    combprodcd = models.IntegerField(null=True)
    flavourcd = models.IntegerField(null=True)
    ema = models.IntegerField(null=True)
    parallel_import = models.IntegerField(null=True)
    avail_restrictcd = models.IntegerField()

    def __unicode__(self):
        return u'[AMP] %s' % self.nm

class ActualMedicinalProductPack(models.Model):
    appid = models.IntegerField(primary_key=True)
    invalid = models.IntegerField(null=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(max_length=255, null=True)
    vppid = models.ForeignKey('VirtualMedicinalProductPack', db_column='vppid')
    apid = models.ForeignKey('ActualMedicinalProduct', db_column='apid')
    combpackcd = models.IntegerField()
    legal_catcd = models.IntegerField()
    subp = models.CharField(max_length=255, null=True)
    disccd = models.IntegerField()
    discdt = models.DateField(null=True)

    def __unicode__(self):
        return u'[AMP] %s' % self.nm