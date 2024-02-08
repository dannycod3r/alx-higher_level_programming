//
$(document).ready(function () {
  // Add click event listener to the DIV#update_header element
  $('DIV#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
