#!/usr/bin/node
/**
 * Write a script that prints the number of movies where
 *       where the character "Wedge Antilles" is present
 * The first argument
 */
const request = require('request');
const apiUrl = process.argv[2];
const charId = '18';

let count = 0;

request(apiUrl, (err, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const bodyObj = JSON.parse(body.body);
  const results = bodyObj.results;

  // get the count for 18
  for (const rkey in bodyObj.results) {
    for (const ckey in results[rkey].characters) {
      if (results[rkey].characters[ckey].includes(charId)) {
        count++;
      }
    }
  }
  console.log(count);
});
