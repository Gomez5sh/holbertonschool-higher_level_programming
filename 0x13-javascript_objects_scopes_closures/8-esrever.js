#!/usr/bin/node
/*
Write a function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  const final = [];
  for (let n = list.length - 1; n >= 0; n--) {
    final.push(list[n]);
  }

  return (final);
};
