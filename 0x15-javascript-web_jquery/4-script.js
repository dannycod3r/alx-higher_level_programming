$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    // Check if the <header> element has the class 'red'
    if ($('header').hasClass('red')) {
      // If it has 'red', remove it and add 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // If it doesn't have 'red', remove 'green' and add 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
