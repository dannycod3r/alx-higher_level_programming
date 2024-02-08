$(document).ready(function () {
  // Fetch movie titles from the API
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Loop through each movie in the fetched data
    $.each(data.results, function (index, movie) {
      // Create a new list item with the movie title and append it to the UL#list_movies
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
