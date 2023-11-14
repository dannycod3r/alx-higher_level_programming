#!/usr/bin/node
// print the first argument
if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv[2]) { // print only the first argument
  console.log(process.argv[2]);
}
