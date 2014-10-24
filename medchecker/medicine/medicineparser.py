from medicine.models import VirtualMedicinalProduct

import re, string

__DOSE_SYMBOL_RE = r'g|ug|mg|kg|l|ml|p|d|s|OP|CP|Mu|u|mg/kg|ml/kg|/kg|cm|in|micrograms'
__STRENGTH_RE = r'([0-9.]+( )*(' + __DOSE_SYMBOL_RE + ')(/([0-9.]( )*)?(' + __DOSE_SYMBOL_RE + '))?(?=( |$|/|\))+))'

__DAILY_REPETITION_SYMBOL_RE = r'd|ad|d3|d4|d5|qw|tw|bw|ow|om|w2|mwf|prn'
__DAILY_REPETITION_RE = r'(^|[^\w\d])+(' + __DAILY_REPETITION_SYMBOL_RE + ')([^\w\d]|$)+'

__INTERVAL_FREQUENCY_SYMBOL_RE = r'hh|h1|h2|h3|h4|h5|h6|h8|h12|h18|h24|hd|pd|qd|td|tid|bd|od'
__INTERVAL_FREQUENCY_RE = r'(^|[^\w\d])+(' + __INTERVAL_FREQUENCY_SYMBOL_RE + ')([^\w\d]|$)+'

__FORM_SYMBOL_RE = r'capsule(s)?|tablet(s)?|bandage(s)?|injection(s)?|drop(s)?|patch(es)?|sachet(s)?|roll(s)?|tube(s)?|suppositor(y)?(ies)?|infusion bag(s)?|vial(s)?|suspension|solution(s)?|ointment(s)?|cream(s)?'
__FORM_RE = r'(^|[^\w\d])+(' + __FORM_SYMBOL_RE + ')([^\w\d]|$)+'

__ROUTE_SYMBOL_RE = r'implant|inhalation|instillation|nasal|oral|parenteral|rectal|sublingual/buccal/oromucosal|transdermal|vaginal|ophthalmic|eye'
__ROUTE_RE = r'(^|[^\w\d])+(' + __ROUTE_SYMBOL_RE + ')([^\w\d]|$)+'

# __MEDICINE_RE = r'^([\w ]*) (?=(,|[0-9]|' + __DOSE_SYMBOL_RE + '|' + __DAILY_REPETITION_SYMBOL_RE + '|' + __INTERVAL_FREQUENCY_SYMBOL_RE + '))'
__MEDICINE_RE = r'^([\w\d %\(\)/.\-]{4,})(?=(,|$))'

INTERVAL_FREQUENCY_HUMAN_MAP = {
    # Interval Frequence
    'hh': 'every 30 minutes',
    'h1': 'every hour',
    'h2': 'every 2 hours',
    'h3': 'every 3 hours',
    'h4': 'every 4 hours',
    'h5': 'every 5 hours',
    'h6': 'every 6 hours',
    'h8': 'every 8 hours',
    'h12': 'every 12 hours',
    'h18': 'every 18 hours',
    'h24': 'every 24 hours',
    'hd': 'six times a day',
    'pd': 'five times a day',
    'qd': 'four times a day',
    'td': 'three times a day',
    'tid': 'three times a day',
    'bd': 'twice a day',
    'od': 'once a day',
    }

DAILY_REPETITION_HUMAN_MAP = {
    'd':  'daily',
    'ad': 'alternate days',
    'd3': 'every 3 days',
    'd4': 'every 4 days',
    'd5': 'every 5 days',
    'qw': 'four times a week',
    'tw': 'twice a week',
    'bw':  'twice a week',
    'ow':  'once a week',
    'om':  'once a month',
    'mwf': 'Monday, Wednesday, Friday',
    'prn': 'as required',
    }

FORM_HUMAN_MAP = {
    'capsule': 'capsule',
    'capsules': 'capsule',
    'tablet': 'tablet',
    'tablets': 'tablet',
    'drop': 'drop',
    'drops': 'drop',
    'bandage': 'bandage',
    'bandages': 'bandage',
    'injection': 'injection',
    'injections': 'injection',
    'patch': 'patch',
    'patches': 'patch',
    'sachet': 'sachet',
    'sachets': 'sachet',
    'roll': 'roll',
    'rolls': 'roll',
    'tube': 'tube',
    'tubes': 'tube',
    'suppository': 'suppository',
    'suppositories': 'suppository',
    'infusion bag': 'infusion bag',
    'infusion bags': 'infusion bag',
    'vial': 'vial',
    'vials': 'vial',
    'suspension': 'suspension',
    'solution': 'solution',
    'solutions': 'solution',
    'ointment': 'ointment',
    'ointments': 'ointment',
    'cream': 'cream',
    'creams': 'cream',
    }

ROUTE_HUMAN_MAP = {
    'implant': 'implant',
    'inhalation': 'inhalation',
    'instillation': 'instillation',
    'nasal': 'nasal',
    'oral': 'oral',
    'parenteral': 'parenteral',
    'rectal': 'rectal',
    'sublingual/buccal/oromucosal': 'sublingual/buccal/oromucosal',
    'transdermal': 'transdermal',
    'vaginal': 'vaginal',
    'eye': 'ophthalmic',
    'ophthalmic': 'ophthalmic',
}

__DOSE_SYNTAX_HUMAN_MAP = dict(
    INTERVAL_FREQUENCY_HUMAN_MAP.items() +
    DAILY_REPETITION_HUMAN_MAP.items() + 
    FORM_HUMAN_MAP.items() + 
    ROUTE_HUMAN_MAP.items()
    )

def clean_token(token, remove_punctuation=True):
    token = token.replace('&nbsp;', ' ')

    if remove_punctuation:
        translation_table = dict((ord(char), None) for char in string.punctuation)
        token = token.translate(translation_table)

    return token.strip()

def normalize_input(input_string):
    for k, v in INTERVAL_FREQUENCY_HUMAN_MAP.items():
        input_string = input_string.replace(v, k)

    for k, v in DAILY_REPETITION_HUMAN_MAP.items():
        input_string = input_string.replace(v, k)

    return input_string

def get_medicine_text_as_components(medicine_text):
    medicine_text_lower = normalize_input(medicine_text)

    medicine_dict = {}

    # Medicine
    m = re.search(__MEDICINE_RE, medicine_text)
    if m:
        medicine_dict['medicine'] = m.group(0)

    # If a potential medicine name is found try and validate it against the 
    # database for a real VMP. 
    if medicine_dict.get('medicine'):
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__iexact=medicine_dict['medicine']
                )

            if vmp is not None:
                medicine_dict['medicine'] = vmp.nm
                medicine_dict['medicine_is_valid'] = True
        except VirtualMedicinalProduct.DoesNotExist:
            medicine_dict['medicine_is_valid'] = False

    # Form
    m = re.search(__FORM_RE, medicine_text_lower)
    if m:
        medicine_dict['form'] = __DOSE_SYNTAX_HUMAN_MAP[clean_token(m.group(0))]

    # Strength
    m = re.search(__STRENGTH_RE, medicine_text_lower)
    if m:
        medicine_dict['strength'] = clean_token(m.group(0), remove_punctuation=False)

    # Frequency
    m = re.search(__INTERVAL_FREQUENCY_RE, medicine_text_lower)
    if m:
        medicine_dict['frequency'] = __DOSE_SYNTAX_HUMAN_MAP[clean_token(m.group(0))]

    # Duration
    m = re.search(__DAILY_REPETITION_RE, medicine_text_lower)
    if m:
        medicine_dict['duration'] = __DOSE_SYNTAX_HUMAN_MAP[clean_token(m.group(0))]

    # Route
    m = re.search(__ROUTE_RE, medicine_text_lower)
    if m:
        medicine_dict['route'] = __DOSE_SYNTAX_HUMAN_MAP[clean_token(m.group(0))]

    # Dose
    medicine_dict['dose'] =  '%s, %s, %s' % (
        medicine_dict.get('strength', '?'), medicine_dict.get('route', '?'),
        medicine_dict.get('frequency', '?')
        )
    

    # # Instructions
    # m = re.search(__DOSE_RE, medicine_text_lower)
    # if m:
    #     interval = m.group(0).lower().strip()
    #     medicine_dict['dose'] = __DOSE_SYNTAX_HUMAN_MAP[interval]

    return medicine_dict