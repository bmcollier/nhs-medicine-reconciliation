// Statics
var marandBaseUrl = "https://rest.ehrscape.com/rest/v1";
var demographicsBaseUrl = "https://rest.ehrscape.com/rest/v1";

// Session Variables

var sessionId;
var demogSessionId;

//  Standard HANDI-HOPD domain
var username = 'handi';
var password = 'RPEcC859';

var returnvals = {hello: 'hello'};
var globalval;

function executeAQL(options) {

	// Keyword Arguments
	var nhsNumber = options.nhsNumber;
	var operation = options.operation || getUKMedications;
	var kwargs = options.kwargs;

	demogLogin().done(function () {
		ehrLogin(marandBaseUrl).done(function () {
        	getPatientEhr(nhsNumber,marandBaseUrl).done(function () {
            	$.when(operation(kwargs)).then(demogLogout());
        	});
    	});	
   });
}
