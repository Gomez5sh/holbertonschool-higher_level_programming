#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie */
const request = require('request');

const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
