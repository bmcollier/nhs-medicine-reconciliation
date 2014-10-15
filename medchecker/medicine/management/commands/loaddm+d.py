from django.core.management.base import BaseCommand

from xml.etree.ElementTree import XML

from medicine.models import (VirtualTherapeuticMoiety, VirtualMedicinalProduct,
    VirtualMedicinalProductPack, ActualMedicinalProduct,
    ActualMedicinalProductPack)
  
def load_dm_and_d():
    # Delete all records we currently have?!?!
    # ActualMedicinalProductPack.objects.all().delete()
    # ActualMedicinalProduct.objects.all().delete()
    # VirtualMedicinalProductPack.objects.all().delete()
    # VirtualMedicinalProduct.objects.all().delete()
    # VirtualTherapeuticMoiety.objects.all().delete()

    load_vtm('C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_vtm2_3091014.xml')
    load_vmp('C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_vmp2_3091014.xml')
    load_vmpp('C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_vmpp2_3091014.xml')
    load_amp('C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_amp2_3091014.xml')
    load_ampp('C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_ampp2_3091014.xml')

def load_vtm(file_location):
    with open(file_location) as vtm_file:
        all_vtm_xml = XML(vtm_file.read())

        for vtm_xml in all_vtm_xml.findall('VTM'):
            vtmid = vtm_xml.find('VTMID')
            invalid = vtm_xml.find('INVALID')
            nm = vtm_xml.find('NM')
            abbrevnm = vtm_xml.find('ABBREVNM')
            vtmidprev = vtm_xml.find('VTMIDPREV')
            vtmiddt = vtm_xml.find('VTMIDDT')

            vtm = VirtualTherapeuticMoiety(vtmid=vtmid.text, nm=nm.text)

            if invalid is not None:
                vtm.invalid = invalid.text

            if abbrevnm is not None:
                vtm.abbrevnm = abbrevnm.text

            if vtmidprev is not None:
                vtm.vtmidprev = vtmidprev.text

            if vtmiddt is not None:
                vtm.vtmiddt = vtmiddt.text

            vtm.save()

def load_vmp(file_location):
    with open(file_location) as vmp_file:
        all_vmp_xml = XML(vmp_file.read())

        for vmp_xml in all_vmp_xml.findall('VMP'):
            vpid = vmp_xml.find('VPID') #
            vpiddt = vmp_xml.find('VPIDDT')
            vpidprev = vmp_xml.find('VPIDPREV')
            vtmid = vmp_xml.find('VTMID') #
            invalid = vmp_xml.find('INVALID')
            nm = vmp_xml.find('NM') #
            abbrevnm = vmp_xml.find('ABBREVNM')
            basiscd = vmp_xml.find('BASISCD') #
            nmdt = vmp_xml.find('NMDT')
            nmprev = vmp_xml.find('NMPREV')
            basis_prevcd = vmp_xml.find('BASIS_PREVCD')
            nmchangecd = vmp_xml.find('NMCHANGECD')
            combprodcd = vmp_xml.find('COMBPRODCD')
            pres_statcd = vmp_xml.find('PRES_STATCD')
            sug_f = vmp_xml.find('SUG_F')
            glu_f = vmp_xml.find('GLU_F')
            pres_f = vmp_xml.find('PRES_F')
            cfc_f = vmp_xml.find('CFC_F')
            non_availcd = vmp_xml.find('NON_AVAILCD')
            non_availdt = vmp_xml.find('NON_AVAILDT')
            df_indcd = vmp_xml.find('DF_INDCD')
            udfs = vmp_xml.find('UDFS')
            udfs_uomcd = vmp_xml.find('UDFS_UOMCD')
            unit_dose_uomcd = vmp_xml.find('UNIT_DOSE_UOMCD')

            vmp = VirtualMedicinalProduct(vpid=vpid.text, vtmid=vtmid.text,
                nm=nm.text, basiscd=basiscd.text
                )

            if vpiddt is not None:
                vmp.vpiddt = vpiddt.text

            if vpidprev is not None:
                vmp.vpidprev = vpidprev.text

            if invalid is not None:
                vmp.invalid = invalid.text

            if abbrevnm is not None:
                vmp.abbrevnm = abbrevnm.text

            if nmdt is not None:
                vmp.nmdt = nmdt.text

            if nmprev is not None:
                vmp.nmprev = nmprev.text

            if basis_prevcd is not None:
                vmp.basis_prevcd = basis_prevcd.text

            if nmchangecd is not None:
                vmp.nmchangecd = nmchangecd.text

            if combprodcd is not None:
                vmp.combprodcd = combprodcd.text

            if pres_statcd is not None:
                vmp.pres_statcd = pres_statcd.text

            if sug_f is not None:
                vmp.sug_f = sug_f.text

            if glu_f is not None:
                vmp.glu_f = glu_f.text

            if pres_f is not None:
                vmp.pres_f = pres_f.text

            if cfc_f is not None:
                vmp.cfc_f = cfc_f.text

            if non_availcd is not None:
                vmp.non_availcd = non_availcd.text

            if non_availdt is not None:
                vmp.non_availdt = non_availdt.text

            if df_indcd is not None:
                vmp.df_indcd = df_indcd.text

            if udfs is not None:
                vmp.udfs = udfs.text

            if udfs_uomcd is not None:
                vmp.udfs_uomcd = udfs_uomcd.text

            if unit_dose_uomcd is not None:
                vmp.unit_dose_uomcd = unit_dose_uomcd.text

            vmp.save()

def load_vmpp(file_location):
    with open(file_location) as vmpp_file:
        all_vmpp_xml = XML(vmpp_file.read())

        for vmpp_xml in all_vmpp_xml.findall('VMPP'):
            vppid = vmpp_xml.find('vppid') #
            invalid = vmpp_xml.find('invalid')
            nm = vmpp_xml.find('nm') # 
            abbrevnm = vmpp_xml.find('abbrevnm')
            vpid = vmpp_xml.find('vpid') #
            qtyval = vmpp_xml.find('qtyval') #
            qty_uomcd = vmpp_xml.find('qty_uomcd') #
            combpackcd = vmpp_xml.find('combpackcd')

            vmpp = VirtualMedicinalProductPack(vppid=vppid.text, nm=nm.text,
                vpid=vpid.tex, qtyval=qtyval.text, qty_uomcd=qty_uomcd.text
                )

            if invalid is not None:
                vmpp.invalid = invalid.text

            if abbrevnm is not None:
                vmpp.abbrevnm = abbrevnm.text

            if combpackcd is not None:
                vmpp.combpackcd = combpackcd.text

            vmpp.save()

def load_amp(file_location):
    with open(file_location) as amp_file:
        all_amp_xml = XML(amp_file.read())

        for amp_xml in all_amp_xml.findall('AMP'):
            apid = amp_xml.get('apid') # 
            invalid = amp_xml.get('INVALID')
            vpid = amp_xml.get('VPID') #
            nm = amp_xml.get('NM') #
            abbrevnm = amp_xml.get('ABBREVNM')
            desc = amp_xml.get('DESC') #
            nmdt = amp_xml.get('NMDT')
            nm_prev = amp_xml.get('NM_PREV')
            suppcd = amp_xml.get('SUPPCD') #
            lic_authcd = amp_xml.get('LIC_AUTHCD') #
            lic_auth_prevcd = amp_xml.get('LIC_AUTH_PREVCD')
            lic_authchangecd = amp_xml.get('LIC_AUTHCHANGECD')
            lic_authchangedt = amp_xml.get('LIC_AUTHCHANGEDT')
            combprodcd = amp_xml.get('COMBPRODCD')
            flavourcd = amp_xml.get('FLAVOURCD')
            ema = amp_xml.get('EMA')
            parallel_import = amp_xml.get('PARALLEL_IMPORT')
            avail_restrictcd = amp_xml.get('AVAIL_RESTRICTCD') #

            amp = ActualMedicinalProduct(apid=apid.text, vpid=vpid.text,
                nm=nm.text, desc=desc.text, suppcd=suppcd.text,
                lic_authcd=lic_authcd.text,
                avail_restrictcd=avail_restrictcd.text
                )

            if invalid is not None:
                amp.invalid = invalid.text

            if abbrevnm is not None:
                amp.abbrevnm = abbrevnm.text

            if nmdt is not None:
                amp.nmdt = nmdt.text

            if nm_prev is not None:
                amp.nm_prev = nm_prev.text

            if lic_auth_prevcd is not None:
                amp.lic_auth_prevcd = lic_auth_prevcd.text

            if lic_authchangecd is not None:
                amp.lic_authchangecd = lic_authchangecd.text

            if lic_authchangedt is not None:
                amp.lic_authchangedt = lic_authchangedt.text

            if combprodcd is not None:
                amp.combprodcd = combprodcd.text

            if flavourcd is not None:
                amp.flavourcd = flavourcd.text

            if ema is not None:
                amp.ema = ema.text

            if parallel_import is not None:
                amp.parallel_import = parallel_import.text

            amp.save()

def load_ampp(file_location):
    with open(file_location) as ampp_file:
        all_ampp_xml = XML(ampp_file.read())

        for ampp_xml in all_ampp_xml.findall('AMPP'):
            appid = ampp_xml.find('APPID') #
            invalid = ampp_xml.find('INVALID')
            nm = ampp_xml.find('NM') #
            abbrevnm = ampp_xml.find('ABBREVNM')
            vppid = ampp_xml.find('VPPID') #
            apid = ampp_xml.find('APID') #
            combpackcd = ampp_xml.find('COMBPACKCD') #
            legal_catcd = ampp_xml.find('LEGAL_CATCD') #
            subp = ampp_xml.find('SUBP')
            disccd = ampp_xml.find('DISCCD') #
            discdt = ampp_xml.find('DISCDT')

            ampp = ActualMedicinalProductPack(appid=appid.text, nm=nm.text,
                vppid=vppid.text, apid=apid.text, combpackcd=combpackcd.text,
                legal_catcd=legal_catcd.text, disccd=disccd.text
                )

            if invalid is not None:
                ampp.invalid = invalid.text

            if abbrevnm is not None:
                ampp.abbrevnm = abbrevnm.text

            if subp is not None:
                ampp.subp = subp.text

            if discdt is not None:
                ampp.discdt = discdt.text


            ampp.save()

class Command(BaseCommand):
    help = 'Loads the dm+d drug database into the django models.'
    
    def handle(self, *args, **options):
        load_dm_and_d()