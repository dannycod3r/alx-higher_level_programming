#!/usr/bin/node
/**
 * Write a script that prints the title of a Star Wars movie
 *       where the episode number matches a given integer
 * The first argument is the movie ID
 */
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com';
const episode = '/api/films' + '/' + process.argv[2];
const url = baseUrl + episode;

request(url, (err, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // convert the body into object
  const bodyObj = JSON.parse(body.body);
  console.log(bodyObj.title);
});
