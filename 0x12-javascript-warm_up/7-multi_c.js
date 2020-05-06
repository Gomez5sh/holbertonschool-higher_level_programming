#!/usr/bin/node
/*
prints statements about c, python, and javascript */
const myVar = process.argv[2];

if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let iter = 0; iter < myVar; iter++) {
    console.log('C is fun');
  }
}
