#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!size) { // if not a number
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let rowLine = '';
    for (let j = 0; j < size; j++) {
      rowLine += 'X';
    }
    console.log(rowLine);
  }
}
