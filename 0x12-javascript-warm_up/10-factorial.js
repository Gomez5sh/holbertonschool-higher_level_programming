#!/usr/bin/node
/*
script that computes and prints a factorial */
const myVar = parseInt(process.argv[2], 10);

function fact (n) {
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * fact(n - 1));
}

console.log(fact(myVar));
