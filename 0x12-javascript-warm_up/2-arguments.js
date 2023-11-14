#!/usr/bin/node
/*
 * Write a script that prints a message depending of the
 * number of arguments passed:
 */

// if no arg -> log “No argument”
// if only 1 or more -> “Argument found"

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
