from django.contrib import admin
from medicine.models import (VirtualTherapeuticMoiety, VirtualMedicinalProduct,
    VirtualMedicinalProductPack, ActualMedicinalProduct,
    ActualMedicinalProductPack)


class DMAndDAdmin(admin.ModelAdmin):
    search_fields = ['nm',]

admin.site.register(VirtualTherapeuticMoiety, DMAndDAdmin)
admin.site.register(VirtualMedicinalProduct, DMAndDAdmin)
admin.site.register(VirtualMedicinalProductPack, DMAndDAdmin)
admin.site.register(ActualMedicinalProduct, DMAndDAdmin)
admin.site.register(ActualMedicinalProductPack, DMAndDAdmin)