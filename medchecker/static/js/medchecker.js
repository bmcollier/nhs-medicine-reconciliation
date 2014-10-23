$('.top-bar img:first').click(function () {
  var openClose = $(this).next().next();
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