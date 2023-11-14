#!/usr/bin/node

const op1 = parseInt(process.argv[2]);
const op2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(op1, op2);
