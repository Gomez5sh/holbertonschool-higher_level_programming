#!/usr/bin/node
/*
 Write a script that prints a square */
const myVar = process.argv[2];

if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let iter = 0; iter < myVar; iter++) {
    console.log('X'.repeat(myVar));
  }
}
