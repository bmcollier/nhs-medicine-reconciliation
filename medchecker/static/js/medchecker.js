function togglePatientMenu() {
  var patientMenu = $('#patient-menu');
  var patientLabel = $('#patient-name').prev();
  if (patientMenu.hasClass('hide')) {
    patientMenu.removeClass('hide');
    $("#patient-name a").css('color', 'rgb(218,220,219)');
    patientLabel.css('color', 'rgb(218,220,219)');
  } else {
    patientMenu.addClass('hide');
    patientLabel.css('color', 'rgb(65, 79, 90)');
    $('#patient-name a').css('color', 'rgb(0, 140, 186)');
  }
}

function toggleUserMenu() {
  var userMenu = $('#user-menu');
  var currentUserNameLabel = $('#current-user-name').prev();
  if (userMenu.hasClass('hide')) {
    userMenu.removeClass('hide');
    $("#current-user-name").css('color', 'rgb(218,220,219)');
    currentUserNameLabel.css('color', 'rgb(218,220,219)');
  } else {
    userMenu.addClass('hide');
    currentUserNameLabel.css('color', 'rgb(65, 79, 90)');
    $('#current-user-name').css('color', 'rgb(65, 79, 90)');
  }
}

function toggleInfoTab() {
  var moreInfo = $('#moreInfo');
  if (moreInfo.hasClass('hide')) {
    moreInfo.removeClass('hide');
  } else {
    moreInfo.addClass('hide');
  }
}

$('#patient-menu-icon').click(function () {
  togglePatientMenu();
});

$('#user-menu-icon').click(function () {
  toggleUserMenu();
});

$('#moreInfoTab').click(function () {
  toggleInfoTab();
});