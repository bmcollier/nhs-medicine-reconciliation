from django.core.management.base import BaseCommand

from xml.etree.ElementTree import XML

from medicine.models import (VirtualTherapeuticMoiety, VirtualMedicinalProduct,
    VirtualMedicinalProductPack, ActualMedicinalProduct,
    ActualMedicinalProductPack)
  
import time

def load_dm_and_d():
    start_time = time.time()

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
    load_ampp(
        ampp_file_location='C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\f_ampp2_3091014.xml',
        gtin_file_location='C:\\Users\\MikeLeonard\\Documents\\MedicineReconcilation\\dm+d\\nhsbsa_dmd_10.1.0_20141013000001\\week422014-r2_3-GTIN\\f_gtin2_0091014.xml'
        )

    end_time = time.time()

    print 'Total Time: %ds' % (end_time - start_time)

def load_vtm(file_location):
    print 'Loading VTMs.'
    counter = 0
    current_pct = 0.0
    start_time = time.time()
    with open(file_location) as vtm_file:
        all_vtm_xml = XML(vtm_file.read())

        all_vtms = all_vtm_xml.findall('VTM')
        total_count = len(all_vtms)

        for vtm_xml in all_vtms:
            vtmid = vtm_xml.find('VTMID')
            invalid = vtm_xml.find('INVALID')
            nm = vtm_xml.find('NM')
            abbrevnm = vtm_xml.find('ABBREVNM')
            vtmidprev = vtm_xml.find('VTMIDPREV')
            vtmiddt = vtm_xml.find('VTMIDDT')

            vtm = VirtualTherapeuticMoiety(vtmid=int(vtmid.text), nm=nm.text)

            if invalid is not None:
                vtm.invalid = invalid.text

            if abbrevnm is not None:
                vtm.abbrevnm = abbrevnm.text

            if vtmidprev is not None:
                vtm.vtmidprev = vtmidprev.text

            if vtmiddt is not None:
                vtm.vtmiddt = vtmiddt.text

            vtm.save()
            counter += 1
            if ((float(counter) / float(total_count)) * 100.0) >= current_pct:
                print ' %d%%' % (current_pct),
                current_pct += 10

    print '... processed %d VTMs in %ds.' % (counter, (time.time() - start_time))

def load_vmp(file_location):
    print 'Loading VMPs.'
    counter = 0
    current_pct = 0.0
    start_time = time.time()
    with open(file_location) as vmp_file:
        all_vmp_xml = XML(vmp_file.read())

        all_vmps = all_vmp_xml.find('VMPS').findall('VMP')

        total_count = len(all_vmps)

        for vmp_xml in all_vmps:
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

            vmp = VirtualMedicinalProduct(vpid=int(vpid.text), nm=nm.text,
                basiscd=basiscd.text
                )

            if vtmid is not None:
                vmp.vtmid_id = int(vtmid.text)

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
            counter += 1
            if ((float(counter) / float(total_count)) * 100.0) >= current_pct:
                print ' %d%%' % (current_pct),
                current_pct += 10

    print '... processed %d VMPs in %ds.' % (counter, (time.time() - start_time))

def load_vmpp(file_location):
    print 'Loading VMPPs.'
    counter = 0
    current_pct = 0.0
    start_time = time.time()
    with open(file_location) as vmpp_file:
        all_vmpp_xml = XML(vmpp_file.read())

        all_vmpps = all_vmpp_xml.find('VMPPS').findall('VMPP')

        total_count = len(all_vmpps)

        for vmpp_xml in all_vmpps:
            vppid = vmpp_xml.find('VPPID') #
            invalid = vmpp_xml.find('INVALID')
            nm = vmpp_xml.find('NM') # 
            abbrevnm = vmpp_xml.find('ABBREVNM')
            vpid = vmpp_xml.find('VPID') #
            qtyval = vmpp_xml.find('QTYVAL') #
            qty_uomcd = vmpp_xml.find('QTY_UOMCD') #
            combpackcd = vmpp_xml.find('COMBPACKCD')

            vmpp = VirtualMedicinalProductPack(vppid=int(vppid.text),
                nm=nm.text, vpid_id=int(vpid.text), qtyval=qtyval.text,
                qty_uomcd=qty_uomcd.text
                )

            if invalid is not None:
                vmpp.invalid = invalid.text

            if abbrevnm is not None:
                vmpp.abbrevnm = abbrevnm.text

            if combpackcd is not None:
                vmpp.combpackcd = combpackcd.text

            vmpp.save()
            counter += 1
            if ((float(counter) / float(total_count)) * 100.0) >= current_pct:
                print ' %d%%' % (current_pct),
                current_pct += 10

    print '... processed %d VMPPs in %ds.' % (counter, (time.time() - start_time))

def load_amp(file_location):
    print 'Loading AMPs.'
    counter = 0
    current_pct = 0.0
    start_time = time.time()
    with open(file_location) as amp_file:
        all_amp_xml = XML(amp_file.read())

        all_amps = all_amp_xml.find('AMPS').findall('AMP')

        total_count = len(all_amps)

        for amp_xml in all_amps:
            apid = amp_xml.find('APID') # 
            invalid = amp_xml.find('INVALID')
            vpid = amp_xml.find('VPID') #
            nm = amp_xml.find('NM') #
            abbrevnm = amp_xml.find('ABBREVNM')
            desc = amp_xml.find('DESC') #
            nmdt = amp_xml.find('NMDT')
            nm_prev = amp_xml.find('NM_PREV')
            suppcd = amp_xml.find('SUPPCD') #
            lic_authcd = amp_xml.find('LIC_AUTHCD') #
            lic_auth_prevcd = amp_xml.find('LIC_AUTH_PREVCD')
            lic_authchangecd = amp_xml.find('LIC_AUTHCHANGECD')
            lic_authchangedt = amp_xml.find('LIC_AUTHCHANGEDT')
            combprodcd = amp_xml.find('COMBPRODCD')
            flavourcd = amp_xml.find('FLAVOURCD')
            ema = amp_xml.find('EMA')
            parallel_import = amp_xml.find('PARALLEL_IMPORT')
            avail_restrictcd = amp_xml.find('AVAIL_RESTRICTCD') #

            amp = ActualMedicinalProduct(apid=int(apid.text),
                vpid_id=int(vpid.text), nm=nm.text, desc=desc.text,
                suppcd=suppcd.text, lic_authcd=lic_authcd.text,
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
            counter += 1
            if ((float(counter) / float(total_count)) * 100.0) >= current_pct:
                print ' %d%%' % (current_pct),
                current_pct += 10

    print '... processed %d AMPs in %ds.' % (counter, (time.time() - start_time))

def load_ampp(ampp_file_location, gtin_file_location):
    print 'Loading AMPPs (including GTIN information).'
    counter = 0
    current_pct = 0.0
    start_time = time.time()

    gtins_dict = {}

    with open(gtin_file_location) as gtin_file:
        print ' Processing GTIN data.'
        all_gtin_xml = XML(gtin_file.read())
        all_gtins = all_gtin_xml.find('AMPPS').findall('AMPP')

        for gtin_xml in all_gtins:
            amppid = gtin_xml.find('AMPPID')
            gtin = gtin_xml.find('./GTINDATA/GTIN')
            startdt = gtin_xml.find('./GTINDATA/STARTDT')
            enddt = gtin_xml.find('./GTINDATA/ENDDT')

            gtin_dict = {'gtin': gtin.text, 'startdt': startdt.text}

            if enddt is not None:
                gtin_dict['enddt'] = enddt.text

            gtins_dict[int(amppid.text)] = gtin_dict


    with open(ampp_file_location) as ampp_file:
        print ' Processing AMPP data.'
        all_ampp_xml = XML(ampp_file.read())
        all_ampps = all_ampp_xml.find('AMPPS').findall('AMPP')
        total_count = len(all_ampps)

    
        for ampp_xml in all_ampps:
            appid = ampp_xml.find('APPID') #
            invalid = ampp_xml.find('INVALID')
            nm = ampp_xml.find('NM') #
            abbrevnm = ampp_xml.find('ABBREVNM')
            vppid = ampp_xml.find('VPPID') #
            apid = ampp_xml.find('APID') #
            combpackcd = ampp_xml.find('COMBPACKCD')
            legal_catcd = ampp_xml.find('LEGAL_CATCD') #
            subp = ampp_xml.find('SUBP')
            disccd = ampp_xml.find('DISCCD')
            discdt = ampp_xml.find('DISCDT')

            ampp = ActualMedicinalProductPack(appid=int(appid.text), nm=nm.text,
                vppid_id=int(vppid.text), apid_id=int(apid.text),
                legal_catcd=legal_catcd.text
                )

            if invalid is not None:
                ampp.invalid = invalid.text

            if abbrevnm is not None:
                ampp.abbrevnm = abbrevnm.text

            if combpackcd is not None:
                ampp.combpackcd = combpackcd.text

            if subp is not None:
                ampp.subp = subp.text

            if disccd is not None:
                ampp.disccd = disccd.text

            if discdt is not None:
                ampp.discdt = discdt.text

            try:
                gtin = gtins_dict[int(appid.text)]

                if gtin.get('gtin') is not None:
                    ampp.gtin = gtin.get('gtin')

                if gtin.get('startdt') is not None:
                    ampp.gtin_startdt = gtin.get('startdt')

                if gtin.get('enddt') is not None:
                    ampp.gtin_enddt = gtin.get('enddt')

            except KeyError:
                pass #print 'No GTIN data found for AMPP %d' % int(appid.text) 


            ampp.save()
            counter += 1
            if ((float(counter) / float(total_count)) * 100.0) >= current_pct:
                print ' %d%%' % (current_pct),
                current_pct += 10

    print '... processed %d AMPPs in %ds.' % (counter, (time.time() - start_time))

class Command(BaseCommand):
    help = 'Loads the dm+d drug database into the django models.'
    
    def handle(self, *args, **options):
        load_dm_and_d()