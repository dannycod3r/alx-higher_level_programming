#!/usr/bin/node
// a script that searches the second biggest
// integer in the list of arguments.

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueArgsSet = new Set(args);
  const uniqueArgs = Array.from(uniqueArgsSet);
  uniqueArgs.sort((a, b) => b - a);
  console.log(uniqueArgs[1]);
}
