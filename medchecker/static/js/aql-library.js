function demogLogin() {
    return $.ajax({
        type: "POST",
        url: demographicsBaseUrl + "/session?" + $.param({username: username, password: password}),
        success: function (res) {
            demogSessionId = res.sessionId;
        }
    });
}

function demogLogout() {
    return $.ajax({
        type: "DELETE",
        url: demographicsBaseUrl + "/session",
        headers: {
            "Ehr-Session": demogSessionId
        }
    });
}

// Get Patient Demographics details from Marand ehrScape 'Party' service
// In a UK setting this may actually be a Spine Mini service call ? with FHIR wrapper
function getPatientDemographics(nhsNumber) {
    return $.ajax({
          url: demographicsBaseUrl + "/demographics/party/" + nhsNumber ,
        type: 'GET',
        headers: {
            "Ehr-Session": demogSessionId
        },
        success: function (data) {
            var party = data.party;
            // Name
            $("#patient-name").html(party.firstNames + ' ' + party.lastNames);
            // NHS Number
            $("#patient-number").html(party.id);

            // Complete age
            var age = getAge(formatDateUS(party.dateOfBirth));
            $(".patient-age").html(age);

            // Date of birth
            $(".patient-dob").html(formatDate(party.dateOfBirth));

            // Age in years
            $(".patient-age-years").html(getAgeInYears(party.dateOfBirth));

            // Gender
            var gender = party.gender;
            $("#patient-gender").html(gender.substring(0, 1) + gender.substring(1).toLowerCase());

            // Address
            var gender = party.gender;
            $("#patient-address").html(party.address.address);

            // Patient's picture
            var imageUrl;
            if (party.hasOwnProperty('partyAdditionalInfo')) {
                party.partyAdditionalInfo.forEach(function (el) {
                    if (el.key === 'image_url') {
                        imageUrl = el.value;
                    }
                });
            }
            if (imageUrl !== undefined) {
                $('.patient-pic').css('background', 'url(' + imageUrl + ')');
            }
        },
        error: function(){alert('Patient ' + ehrId + ' not found');}

    });
}

function ehrLogin(ehrBaseUrl) {
    return $.ajax({
        type: "POST",
		url: ehrBaseUrl + "/session?" + $.param({username: username, password: password}),
    	success: function (res) {
        	sessionId = res.sessionId;
		    if (ehrBaseUrl == marandBaseUrl)
		    {
		        marandSessionId = sessionId;
		    }
		    else
		    {
            	oceanSessionId = sessionId;
        	}
    	}
	});
}

// Formats AQL statement
function formatPatientQuery(aqlstring) {
    return "/query/?aql=" + encodeURIComponent(aqlstring.replace("EHR e" , "EHR e [ehr_id ='"+ ehrId +"'] "));
}

function getPatientEhr(nhsNumber,ehrBaseUrl) {
    return $.ajax({
        url: ehrBaseUrl + "/ehr/?" + $.param({subjectId: nhsNumber, subjectNamespace:'ehscape'}),
        type: 'GET',
        headers: {
            "Ehr-Session": sessionId
        },
        success: function (data) {
            var party = data;
            ehrId = party.ehrId
        },
        error: function(){alert('Service :' + ehrBaseUrl + 'EHRId for Patient NHS Number '+ nhsNumber +' not found');}

    });
}

function serverSuffix(pEhrBaseUrl) {
    if (pEhrBaseUrl == marandBaseUrl)
    {
        return "_m"
    }
    else
    {
        return "_o"
    }
}