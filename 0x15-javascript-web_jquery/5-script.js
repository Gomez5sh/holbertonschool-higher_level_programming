// Write a Javascript script that adds a LI element 
$(document).ready(function () {
    $('#add_item').click(function () {
      $('UL.my_list').append('<li>Item</li>');
    });
  });
