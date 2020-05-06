#!/usr/bin/node
/*
Write a script that prints a message
depending of the number of arguments passed */
const myVar = process.argv.length;

if (myVar < 3) {
  console.log('No argument');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
