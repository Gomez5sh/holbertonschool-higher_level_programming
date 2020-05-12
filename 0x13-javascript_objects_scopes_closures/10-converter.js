#!/usr/bin/node
/* Write a function that converts a number from base 10 */
exports.converter = function (base) {
  return function (trans) {
    return trans.toString(base);
  };
};
