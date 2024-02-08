//
$(document).ready(function () {
  // Fetch character name from the API
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Update the text of the DIV#character element with the fetched name
    $('DIV#character').text(data.name);
  });
});
