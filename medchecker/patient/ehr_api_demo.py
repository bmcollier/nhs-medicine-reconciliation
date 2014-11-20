from ehr_api import aql_request

demographics_url = 'https://rest.ehrscape.com/rest/v1'
ehr_url = 'https://rest.ehrscape.com/rest/v1'
username = 'handi'
password = 'RPEcC859'
aql_statement = ("select "
                    "a/uid/value as uid,"
                    "a_b/items[at0001]/value/value as medName,"
                    "a_b/items[at0001]/value/defining_code/code_string as medCode,"
                    "a_b/items[at0001]/value/defining_code/terminology_id/value as CodeTerminology,"
                    "a_b/items[at0001]/value/mappings/target[terminology_id = 'dm+d']/code_string as dmdCode,"
                    "a_b/items[at0019]/items[at0003]/value/value as medDose,"
                    "m_s/items[at0070, 'Last issued']/items[at0047]/value/value as lastIssueDate "
                "from EHR e "
                "contains COMPOSITION a "
                "contains (INSTRUCTION a_a[openEHR-EHR-INSTRUCTION.medication_order_uk.v1] "
                "contains "
                    "CLUSTER a_b[openEHR-EHR-CLUSTER.medication_item.v1] "
                    "and "
                    "CLUSTER m_s[openEHR-EHR-CLUSTER.medication_status.v1]) "
                "where m_s/items[at0030]/value/defining_code/code_string='at0033'")

print aql_request(demographics_url, ehr_url, 746, aql_statement, username, password)