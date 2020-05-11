#!/usr/bin/node
/*
Write a class Square
*/
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      console.log((c.repeat(this.width)));
    }
  }
};
