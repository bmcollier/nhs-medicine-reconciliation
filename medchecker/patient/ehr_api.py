import requests

def aql_request(demographics_url, ehr_url, nhs_number, aql_statement, username, password):
    session_id = demographics_login(demographics_url, username, password) 
    ehr_data = get_patient_ehr(ehr_url, 746,session_id)
    ehr_id = ehr_data['ehrId']
    aql_in = format_patient_query(aql_statement, ehr_id)
    meds_data = get_uk_medications(aql_in, ehr_url, session_id)
    return meds_data

def demographics_login(demographics_url, username, password):
    payload = {'username': username, 'password': password }
    r = requests.post(demographics_url + "/session", params=payload)
    response = r.json()
    session_id = response['sessionId']
    return session_id
    
def demographics_logout(demographics_url, session_id):
    headers = {'Ehr-Session': session_id }
    r = requests.delete(demographics_url + "/session", headers=headers)   
    return r.status_code
    
def get_patient_demographics():
    pass
    
def ehr_login(ehr_url, username, password):
    payload = {'username': username, 'password': password }
    r = requests.post(ehr_url + "/session", params=payload)
    response = r.json()
    session_id = response['sessionId']
    return session_id
    
def format_patient_query(aqlstring, ehr_id):
    return aqlstring.replace("EHR e" , "EHR e [ehr_id ='"+ ehr_id +"'] ")
    
def get_patient_ehr(ehr_url, nhs_number,session_id):
    payload = {'subjectId': nhs_number, 'subjectNamespace': 'ehscape'}
    headers = {'Ehr-Session': session_id }
    r = requests.get(ehr_url + '/ehr', params=payload, headers=headers)
    return r.json()

def server_suffix():
    pass
    
def get_uk_medications(aqlstatement, ehr_url, session_id):
    headers = {'Ehr-Session': session_id }
    payload = {'aql': aqlstatement}
    r = requests.get(ehr_url + '/query', params=payload, headers=headers)
    return r.json()