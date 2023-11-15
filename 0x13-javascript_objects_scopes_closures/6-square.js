#!/usr/bin/node
//
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
