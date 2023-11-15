#!/usr/bin/node
//
const PSquare = require('./5-square');

class Square extends PSquare {
  // instance method
  charPrint (c) {
    const ch = c || 'X'; // c undefined

    for (let i = 0; i < this.height; i++) {
      let widthLine = '';
      for (let i = 0; i < this.width; i++) {
        widthLine += ch;
      }
      console.log(widthLine);
    }
  }
}

module.exports = Square;
