function getUKMedications(options) {

	var ehrBaseUrl = options.ehrBaseUrl;
	var target = options.target;

    aqlStatement = "select \
        a/uid/value as uid,\
        a_b/items[at0001]/value/value as medName,\
        a_b/items[at0001]/value/defining_code/code_string as medCode,\
        a_b/items[at0001]/value/defining_code/terminology_id/value as CodeTerminology,\
        a_b/items[at0001]/value/mappings/target[terminology_id = 'dm+d']/code_string as dmdCode,\
        a_b/items[at0019]/items[at0003]/value/value as medDose,\
        m_s/items[at0070, 'Last issued']/items[at0047]/value/value as lastIssueDate\
    from EHR e \
        contains COMPOSITION a \
        contains (INSTRUCTION a_a[openEHR-EHR-INSTRUCTION.medication_order_uk.v1]\
        contains \
            CLUSTER a_b[openEHR-EHR-CLUSTER.medication_item.v1]\
               and\
            CLUSTER m_s[openEHR-EHR-CLUSTER.medication_status.v1])\
    where m_s/items[at0030]/value/defining_code/code_string='at0033'";

    return $.ajax({
        url: ehrBaseUrl + formatPatientQuery(aqlStatement),
        type: 'GET',
        headers: {
            "Ehr-Session": sessionId
        },
        success: function (res) {
            for (var i = 0; i < res.resultSet.length; i++) {
                target.append('<li>' + res.resultSet[i].medName + '</li>');
            }
        },
        error: function(){alert('fail');}
    });
}