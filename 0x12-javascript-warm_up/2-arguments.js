#!/usr/bin/node
/*
 * Write a script that prints a message depending of the
 * number of arguments passed:
 */

// if no arg -> log “No argument”
// if only 1 or more -> “Argument found"

// Subtract 2 to exclude 'node' and script path
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
