from django.db import models
from django.core.validators import RegexValidator

class VirtualTherapeuticMoiety(models.Model):
    vtmid = models.BigIntegerField(primary_key=True)
    invalid = models.BigIntegerField(null=True, blank=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, blank=True, max_length=255)
    vtmidprev = models.CharField(null=True, blank=True, max_length=255)
    vtmiddt = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Virtual Therapeutic Moiety'
        verbose_name_plural = 'Virtual Therapeutic Moieties'

    def __unicode__(self):
        return u'[VTM] %s' % self.nm

class VirtualMedicinalProduct(models.Model):
    vpid = models.BigIntegerField(primary_key=True)
    vpiddt = models.DateField(null=True, blank=True)
    vpidprev = models.BigIntegerField(null=True, blank=True)
    vtmid = models.ForeignKey('VirtualTherapeuticMoiety', db_column='vtmid', null=True, blank=True)
    invalid = models.BigIntegerField(null=True, blank=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, blank=True, max_length=255)
    basiscd = models.BigIntegerField()
    nmdt = models.DateField(null=True, blank=True)
    nmprev = models.CharField(null=True, blank=True, max_length=255)
    basis_prevcd = models.BigIntegerField(null=True, blank=True)
    nmchangecd = models.BigIntegerField(null=True, blank=True) 
    combprodcd = models.BigIntegerField(null=True, blank=True)
    pres_statcd = models.BigIntegerField()
    sug_f = models.BigIntegerField(null=True, blank=True)
    glu_f = models.BigIntegerField(null=True, blank=True)
    pres_f = models.BigIntegerField(null=True, blank=True)
    cfc_f = models.BigIntegerField(null=True, blank=True)
    non_availcd = models.BigIntegerField(null=True, blank=True)
    non_availdt = models.DateField(null=True, blank=True)
    df_indcd = models.BigIntegerField(null=True, blank=True) 
    udfs = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=3)
    udfs_uomcd = models.BigIntegerField(null=True, blank=True)
    unit_dose_uomcd = models.BigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Virtual Medicinal Product'

    def __unicode__(self):
        return u'[VMP] %s' % self.nm

class VirtualMedicinalProductPack(models.Model):
    vppid = models.BigIntegerField(primary_key=True)
    invalid = models.BigIntegerField(null=True, blank=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(null=True, blank=True, max_length=255)
    vpid = models.ForeignKey('VirtualMedicinalProduct', db_column='vpid')
    qtyval = models.DecimalField(max_digits=7, decimal_places=2)
    qty_uomcd = models.BigIntegerField()
    combpackcd = models.BigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Virtual Medicinal Product Pack'

    def __unicode__(self):
        return u'[VMPP] %s' % self.nm

class ActualMedicinalProduct(models.Model):
    apid = models.BigIntegerField(primary_key=True)
    invalid = models.BigIntegerField(null=True, blank=True)
    vpid = models.ForeignKey('VirtualMedicinalProduct', db_column='vpid')
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(max_length=255, null=True, blank=True)
    desc = models.CharField(max_length=255)
    nmdt = models.DateField(null=True, blank=True)
    nm_prev = models.CharField(max_length=255, null=True, blank=True)
    suppcd = models.BigIntegerField()
    lic_authcd = models.BigIntegerField()
    lic_auth_prevcd = models.BigIntegerField(null=True, blank=True)
    lic_authchangecd = models.BigIntegerField(null=True, blank=True)
    lic_authchangedt = models.DateField(null=True, blank=True)
    combprodcd = models.BigIntegerField(null=True, blank=True)
    flavourcd = models.BigIntegerField(null=True, blank=True)
    ema = models.BigIntegerField(null=True, blank=True)
    parallel_import = models.BigIntegerField(null=True, blank=True)
    avail_restrictcd = models.BigIntegerField()

    class Meta:
        verbose_name = 'Actual Medicinal Product'

    def __unicode__(self):
        return u'[AMP] %s' % self.nm

class ActualMedicinalProductPack(models.Model):
    appid = models.BigIntegerField(primary_key=True)
    invalid = models.BigIntegerField(null=True, blank=True)
    nm = models.CharField(max_length=255)
    abbrevnm = models.CharField(max_length=255, null=True, blank=True)
    vppid = models.ForeignKey('VirtualMedicinalProductPack', db_column='vppid')
    apid = models.ForeignKey('ActualMedicinalProduct', db_column='apid')
    combpackcd = models.BigIntegerField(null=True, blank=True)
    legal_catcd = models.BigIntegerField()
    subp = models.CharField(max_length=255, null=True, blank=True)
    disccd = models.BigIntegerField(null=True, blank=True)
    discdt = models.DateField(null=True, blank=True)
    # Barcode data below
    gtin = models.CharField(max_length=14, null=True, blank=True, validators=[RegexValidator(regex=r'|([0-9]{13})|([0-9]{14})', message="GTIN must be 13 or 14 digits.")])
    gtin_startdt = models.DateField(null=True, blank=True)
    gtin_enddt = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name = 'Actual Medicinal Product Pack'

    def __unicode__(self):
        return u'[AMPP] %s' % self.nm