#!/usr/bin/node
/**
 * Write a script that gets the contents of a webpage and stores it in a file.
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 */
const fs = require('node:fs');
const request = require('request');

// get the webpage
request(process.argv[2], (err, page) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(process.argv[3], page.body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
