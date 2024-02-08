//
$(document).ready(function () {
  // Fetch translation of "hello" from the API
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update the text of the DIV#hello element with the fetched translation
    $('DIV#hello').text(data.hello);
  });
});
