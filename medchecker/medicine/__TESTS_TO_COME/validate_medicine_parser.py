from gp_prescriptions import GP_PRESCRIPTIONS
from medicineparser import get_medicine_text_as_components

for prescription in GP_PRESCRIPTIONS:
    result = get_medicine_text_as_components(prescription)
    print prescription
    print '    medicine: ' + result.get('medicine', '-?-')
    print '    daily_repetition: ' + result.get('daily_repetition', '-?-')
    print '    interval_frequency: ' + result.get('interval_frequency', '-?-')
    print ''