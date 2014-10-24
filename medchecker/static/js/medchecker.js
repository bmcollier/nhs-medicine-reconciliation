$('#patient-menu-icon').click(function () {
  var openClose = $('#patient-menu');
  var patientLabel = $('#patient-name').prev();
  if (openClose.hasClass('hide')) {
    openClose.removeClass('hide');
    $("#patient-name a").css('color', 'rgb(218,220,219)');
    patientLabel.css('color', 'rgb(218,220,219)');
  } else {
    openClose.addClass('hide');
    patientLabel.css('color', 'rgb(65, 79, 90)');
    $('#patient-name a').css('color', 'rgb(0, 140, 186)');
  }
});

$('#user-menu-icon').click(function () {
  var openClose = $('#user-menu');
  var currentUserNameLabel = $('#current-user-name').prev();
  if (openClose.hasClass('hide')) {
    openClose.removeClass('hide');
    $("#current-user-name").css('color', 'rgb(218,220,219)');
    currentUserNameLabel.css('color', 'rgb(218,220,219)');
  }
  else {
    openClose.addClass('hide');
    currentUserNameLabel.css('color', 'rgb(65, 79, 90)');
    $('#current-user-name').css('color', 'rgb(65, 79, 90)');
  }
});

$('#moreInfoTab').click(function () {
  var openClose = $('#moreInfo');
  if (openClose.hasClass('hide')) {
    openClose.removeClass('hide');
  }
  else {
    openClose.addClass('hide');
  }
});