#!/usr/bin/node
/*
Write a script that prints My number */
const intRegex = /^[0-9]*?.[0-9]*$/;

if (intRegex.test(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
