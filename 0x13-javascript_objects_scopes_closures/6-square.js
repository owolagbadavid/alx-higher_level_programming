#!/usr/bin/node

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {

  charPrint (c = 'X') {
    super.print(c);
  }
};
