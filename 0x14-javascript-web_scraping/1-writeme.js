#!/usr/bin/node
/*
Write a script that display the status code  */
const fs = require('fs');
const file = process.argv[2];
const file2 = process.argv[3];

fs.writeFile(file, file2, function (err) {
  if (err) {
    console.log(err);
  }
});
