#!/usr/bin/node
/*
Write a script that computes and prints a factorial */
const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
let container;

function add (myVar1, myVar2) {
  container = parseInt(myVar1) + parseInt(myVar2);
  console.log(container);
}

add(myVar1, myVar2);
