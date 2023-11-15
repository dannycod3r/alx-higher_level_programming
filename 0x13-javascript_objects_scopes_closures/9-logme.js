#!/usr/bin/node
//
let argumentCount = 0; // global scope

exports.logMe = function (item) {
  // Log the current count and the value of the argument
  console.log(`${argumentCount}: ${item}`);

  // Increment the counter for the next call
  argumentCount++;
};
