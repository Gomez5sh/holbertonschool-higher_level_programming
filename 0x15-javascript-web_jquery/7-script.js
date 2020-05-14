//Write a Javascript script that fetches and replaces the name
$(document).ready(function () {
    $.get('https://swapi.co/api/people/5/?format=json', function (data) {
      $('#character').html(data.name);
    });
  });