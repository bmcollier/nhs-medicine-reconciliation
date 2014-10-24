from django.db import models
from django.core.validators import RegexValidator

from medicine.models import VirtualMedicinalProduct

import time, random, string

def generate_hospital_id():
    return str(int(time.time() * 10))

def generate_nhs_number():
    return random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + ' ' + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + ' ' + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)

def generate_first_name():
    first_name = ['Kenyon', 'Joelle', 'Sylvester', 'Shay', 'Hamilton', 'Scarlet', 'MacKenzie', 'Gisela', 'Althea', 'Alice', 'Tatum', 'Chandler', 'Wing', 'Honorato', 'Yardley', 'Mariko', 'Latifah', 'Lysandra', 'Sonya', 'May', 'Lana', 'Beau', 'Jason', 'Ifeoma', 'Shaeleigh', 'Magee', 'Zelenia', 'Stacy', 'Thaddeus', 'Clare', 'Blake', 'Lila', 'Charde', 'Kyle', 'Arsenio', 'Dai', 'Riley', 'Charles', 'Hiroko', 'Kirsten', 'Nicole', 'Theodore', 'Sydney', 'Dorothy', 'Alan', 'Myles', 'Victor', 'Paul', 'Victor', 'Marsden', 'Karly', 'Magee', 'Rinah', 'Maris', 'Mara', 'Laurel', 'Lunea', 'Thaddeus', 'Illana', 'Winter', 'Lana', 'Lucy', 'Zenia', 'Neil', 'Lee', 'Virginia', 'Georgia', 'Maya', 'Britanni', 'Jeanette', 'Clare', 'Abdul', 'Chava', 'Shafira', 'Brett', 'Orli', 'Yasir', 'Jamal', 'Nash', 'Timon', 'Silas', 'Moses', 'Ishmael', 'Evan', 'Lana', 'Ignatius', 'Nora', 'Alexander', 'Amethyst', 'Hasad', 'Iliana', 'Bree', 'Uma', 'Neville', 'Alexa', 'John', 'Gisela', 'Xerxes', 'Delilah', 'Nell']
    return random.choice(first_name)

def generate_last_name():
    last_name = ['Haynes', 'Vincent', 'Campbell', 'Martin', 'Blankenship', 'Leonard', 'Randolph', 'Trevino', 'Camacho', 'Turner', 'Contreras', 'Burgess', 'Rosa', 'Lott', 'Craig', 'Norman', 'Ryan', 'Dunlap', 'Diaz', 'Tanner', 'Hancock', 'Webster', 'Santiago', 'Ortiz', 'Ramirez', 'Nieves', 'Moreno', 'Glenn', 'Knight', 'Horn', 'Mayer', 'Burris', 'Duffy', 'Cote', 'Franks', 'Kim', 'Rojas', 'Ballard', 'Morton', 'Erickson', 'Crane', 'Dyer', 'Adkins', 'Villarreal', 'Perkins', 'Burnett', 'Davis', 'Aguirre', 'Bowers', 'Rios', 'Boyd', 'Silva', 'Hahn', 'King', 'Bright', 'Browning', 'Stephens', 'Moses', 'Merritt', 'Pate', 'Goodman', 'Munoz', 'Nichols', 'Ayala', 'Mckee', 'Wong', 'Jarvis', 'Edwards', 'Moran', 'Long', 'Lucas', 'Logan', 'Luna', 'Gonzales', 'Alexander', 'Rosales', 'Meyer', 'Duffy', 'Duran', 'Olson', 'Pierce', 'Garza', 'Cabrera', 'Hampton', 'Rollins', 'Cherry', 'Mcdonald', 'Hardin', 'Lott', 'Washington', 'Zamora', 'Branch', 'Odonnell', 'Henderson', 'Lopez', 'Gilmore', 'Marshall', 'Salazar', 'Nolan', 'Weiss']
    return random.choice(last_name)

def generate_street():
    pre_street = ['Amber', 'Acorn', 'Acres', 'Auburn', 'Anchor', 'Alcove', 'Bent', 'Apple', 'Arbor', 'Big', 'Autumn', 'Avenue', 'Birch', 'Axe', 'Bank', 'Blue', 'Barn', 'Bayou', 'Bright', 'Beacon', 'Bend', 'Broad', 'Bear', 'Bluff', 'Burning', 'Beaver', 'Byway', 'Calm', 'Berry', 'Canyon', 'Cinder', 'Bird', 'Chase', 'Clear', 'Blossom', 'Circle', 'Cold', 'Bluff', 'Corner', 'Colonial', 'Branch', 'Court', 'Cool', 'Bridge', 'Cove', 'Cotton', 'Brook', 'Crest', 'Cozy', 'Butterfly', 'Cut', 'Crimson', 'Butternut', 'Dale', 'Crystal', 'Castle', 'Dell', 'Dewy', 'Chestnut', 'Drive', 'Dusty', 'Cider', 'Edge', 'Easy', 'Cloud', 'Estates', 'Emerald', 'Cottage', 'Falls', 'Fallen', 'Creek', 'Farms', 'Foggy', 'Crow', 'Field', 'Gentle', 'Dale', 'Flats', 'Golden', 'Deer', 'Gardens', 'Grand', 'Diamond', 'Gate', 'Green', 'Dove', 'Glade', 'Happy', 'Elk', 'Glen', 'Harvest', 'Elm', 'Grove', 'Hazy', 'Embers', 'Haven', 'Heather', 'Fawn', 'Heights', 'Hidden', 'Feather', 'Highlands', 'High', 'Flower', 'Hollow', 'Honey', 'Forest', 'Isle', 'Hush', 'Fox', 'Jetty', 'Indian', 'Gate', 'Journey', 'Iron', 'Goat', 'Knoll', 'Ivory', 'Goose', 'Lace', 'Jagged', 'Grove', 'Lagoon', 'Lazy', 'Harbor', 'Landing', 'Little', 'Hickory', 'Lane', 'Lone', 'Hills', 'Ledge', 'Lonely', 'Holly', 'Manor', 'Long', 'Horse', 'Meadow', 'Lost', 'Island', 'Mews', 'Merry', 'Lake', 'Niche', 'Middle', 'Lamb', 'Nook', 'Misty', 'Leaf', 'Orchard', 'Noble', 'Log', 'Pace', 'Old', 'Maple', 'Park', 'Orange', 'Mill', 'Pass', 'Pearl', 'Mountain', 'Path', 'Pied', 'Nectar', 'Pike', 'Pleasant', 'Nest', 'Place', 'Pretty', 'Nut', 'Point', 'Quaint', 'Oak', 'Promenade', 'Quaking', 'Panda', 'Quay', 'Quiet', 'Peach', 'Race', 'Red', 'Pebble', 'Ramble', 'Rocky', 'Pine', 'Ridge', 'Rose', 'Pioneer', 'Road', 'Rough', 'Pond', 'Round', 'Round', 'Pony', 'Rove', 'Rustic', 'Prairie', 'Run', 'Sandy', 'Pumpkin', 'Saunter', 'Shady', 'Quail', 'Shoal', 'Silent', 'Rabbit', 'Stead', 'Silver', 'Rise', 'Street', 'Sleepy', 'River', 'Stroll', 'Small', 'Robin', 'Summit', 'Square', 'Rock', 'Swale', 'Still', 'Shadow', 'Terrace', 'Stony', 'Sky', 'Trace', 'Strong', 'Snake', 'Trail', 'Sunny', 'Spring', 'Trek', 'Sweet', 'Squirrel', 'Turn', 'Tawny', 'Stone', 'Twist', 'Tender', 'Swan', 'Vale', 'Thunder', 'Timber', 'Valley', 'Turning', 'Treasure', 'View', 'Twin', 'Turtle', 'Villa', 'Umber', 'View', 'Vista', 'Velvet', 'Wagon', 'Wander', 'White', 'Willow', 'Way', 'Windy', 'Zephyr', 'Woods', ]
    post_street = ['Street', 'Lane', 'Road', 'Avenue', 'Oval', 'Circuit', 'Way']
    street_no = str(int(random.random() * random.random() * 500))
    return street_no + ' ' + random.choice(pre_street) + ' ' + random.choice(post_street)

def generate_town():
    towns = ['Aberdeen', 'Armagh', 'Bangor', 'Bath', 'Belfast', 'Birmingham', 'Bradford', 'Brighton and Hove', 'Bristol', 'Cambridge', 'Canterbury', 'Cardiff', 'Carlisle', 'Chester', 'Chichester', 'City of London', 'Coventry', 'Derby', 'Dundee', 'Durham', 'Edinburgh', 'Ely', 'Exeter', 'Glasgow', 'Gloucester', 'Hereford', 'Inverness', 'Kingston upon Hull', 'Lancaster', 'Leeds', 'Leicester', 'Lichfield', 'Lincoln', 'Lisburn', 'Liverpool', 'Londonderry', 'Manchester', 'Newcastle upon Tyne', 'Newport', 'Newry', 'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth', 'Preston', 'Ripon', 'Salford', 'Salisbury', 'Sheffield', 'Southampton', 'St Albans', 'St Davids', 'Stirling', 'Stoke-on-Trent', 'Sunderland', 'Swansea', 'Truro', 'Wakefield', 'Wells', 'Westminster', 'Winchester', 'Wolverhampton', 'Worcester', 'York']
    return random.choice(towns)

def generate_county():
    counties = ['Greater London', 'West Midlands', 'Greater Manchester', 'West Yorkshire', 'Merseyside', 'South Yorkshire', 'Tyne and Wear', 'Kent', 'Essex', 'Hampshire', 'Lancashire', 'Surrey', 'Hertfordshire', 'Norfolk', 'Staffordshire', 'West Sussex', 'Nottinghamshire', 'Derbyshire', 'Devon', 'Suffolk', 'Lincolnshire', 'Northamptonshire', 'Oxfordshire', 'Leicestershire', 'Cambridgeshire', 'North Yorkshire', 'Gloucestershire', 'Worcestershire', 'Warwickshire', 'Somerset', 'East Sussex', 'Buckinghamshire', 'Cumbria', 'Dorset', 'Cornwall', 'County Durham', 'Wiltshire', 'Bristol', 'Cheshire East', 'East Riding of Yorkshire', 'Leicester', 'Cheshire West and Chester', 'Northumberland', 'Shropshire', 'Nottingham', 'Brighton & Hove', 'Medway', 'South Gloucestershire', 'Plymouth', 'Hull', 'Central Bedfordshire', 'Milton Keynes', 'Derby', 'Stoke-on-Trent', 'Southampton', 'Swindon', 'Portsmouth', 'Luton', 'North Somerset', 'Warrington', 'York', 'Stockton-on-Tees', 'Peterborough', 'Herefordshire', 'Bournemouth', 'Bath and North East Somerset', 'Southend-on-Sea', 'North Lincolnshire', 'Telford and Wrekin', 'North East Lincolnshire', 'Thurrock', 'Bedford', 'Reading', 'Wokingham', 'West Berkshire', 'Poole', 'Blackburn with Darwen', 'Windsor and Maidenhead', 'Blackpool', 'Slough', 'Middlesbrough', 'Isle of Wight', 'Redcar and Cleveland', 'Torbay', 'Halton', 'Bracknell Forest', 'Darlington', 'Hartlepool', 'Rutland', 'Isles of Scilly']
    return random.choice(counties)

def generate_postcode():
    return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.digits) + ' ' + random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)


class GeneralPractitioner(models.Model):
    first_name = models.CharField(max_length=255, default=generate_first_name)
    last_name = models.CharField(max_length=255, default=generate_last_name)
    street = models.CharField(max_length=255, default=generate_street)
    town = models.CharField(max_length=255, default=generate_town)
    county = models.CharField(max_length=255, default=generate_county)
    post_code = models.CharField(max_length=255, default=generate_postcode)

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.get_full_name()

def get_random_gp():
    try:
        return GeneralPractitioner.objects.order_by('?')[0].id
    except IndexError:
        return None

class Patient(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    hospital_id = models.CharField(max_length=100, default=generate_hospital_id, unique=True, editable=False)
    nhs_number = models.CharField(max_length=12, default=generate_nhs_number, validators=[RegexValidator(regex=r'[0-9]{3} [0-9]{3} [0-9]{4}', message='NHS Number must be in the format 000 000 0000')])
    first_name = models.CharField(max_length=255, default=generate_first_name)
    last_name = models.CharField(max_length=255, default=generate_last_name)
    date_of_birth = models.DateField()
    address = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    general_practitioner = models.ForeignKey(GeneralPractitioner, default=get_random_gp)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.nhs_number)

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

class PatientMedication(models.Model):
    SOURCE_CHOICES = (
        ('RELATIVE', 'Relative of Patient'),
        ('CARER', 'Carer of Patient'),
        ('PATIENT', 'Patient'),
        ('MEDICINE_BAG', 'Medicine Bag'),
        )

    STATUS_CHOICES = (
        ('0 UNVERIFIED', 'Unverified'),
        ('1 TAKING', 'Taking as prescribed'),
        ('1 NOT AS PRESCRIBED', 'Taking, but not as prescribed'),
        ('1 NOT TAKING', 'Not Taking'),
        ('2 DELETED', 'Deleted'),
        )

    patient = models.ForeignKey(Patient, blank=True, null=True)
    virtual_medicinal_product = models.ForeignKey(VirtualMedicinalProduct, null=True)
    free_text = models.CharField(max_length=1000, null=True, blank=True)
    form = models.CharField(max_length=255, null=True, blank=True)
    strength = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255)
    dose = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True, blank=True)
    special_instructions = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    reason = models.CharField(max_length=1000, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='0 UNVERIFIED')

    def __unicode__(self):
        return u'%s - %s (%s)' % (self.patient.get_full_name(), self.virtual_medicinal_product.nm, self.source)

    def is_verified(self):
        if self.status == '0 UNVERIFIED':
            return False

        return True

class GPMedication(models.Model):
    STATUS_CHOICES = (
        ('UNVERIFIED', 'Unverified'),
        ('VERIFIED', 'Verified'),
        ('DELETED', 'Deleted'),
        )

    patient = models.ForeignKey(Patient, blank=True, null=True)
    virtual_medicinal_product = models.ForeignKey(VirtualMedicinalProduct, null=True)
    form = models.CharField(max_length=255, null=True, blank=True)
    strength = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255)
    dose = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True, blank=True)
    special_instructions = models.TextField(null=True, blank=True)
    reason = models.CharField(max_length=1000, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __unicode__(self):
        return u'%s - %s (GP)' % (self.patient.get_full_name(), self.virtual_medicinal_product.nm)