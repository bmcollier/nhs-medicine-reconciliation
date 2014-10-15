from django.contrib import admin
from medicine.models import (VirtualTherapeuticMoiety, VirtualMedicinalProduct,
    VirtualMedicinalProductPack, ActualMedicinalProduct,
    ActualMedicinalProductPack)

admin.site.register(VirtualTherapeuticMoiety)
admin.site.register(VirtualMedicinalProduct)
admin.site.register(VirtualMedicinalProductPack)
admin.site.register(ActualMedicinalProduct)
admin.site.register(ActualMedicinalProductPack)