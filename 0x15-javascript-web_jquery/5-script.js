//
$(document).ready(function () {
  // Add click event listener to the DIV#add_item element
  $('DIV#add_item').click(function () {
    // Create a new <li> element with text 'Item'
    const newItem = $('<li>Item</li>');
    // Append the new <li> element to UL.my_list
    $('UL.my_list').append(newItem);
  });
});
