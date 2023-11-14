#!/usr/bin/node

let number = process.argv[2];

if (!number) {
  number = 0;
}

function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

console.log(factorial(number));
