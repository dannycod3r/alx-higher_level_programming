#!/usr/bin/node
//

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method print
  print () {
    for (let i = 0; i < this.height; i++) {
      let widthLine = '';
      for (let j = 0; j < this.width; j++) {
        widthLine += 'X';
      }
      console.log(widthLine);
    }
  }

  // instance method
  rotate () { // swap using destructuring assignment
    [this.width, this.height] = [this.height, this.width];
  }

  // instance method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
