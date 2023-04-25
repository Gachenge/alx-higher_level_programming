#!/usr/bin/node
/**
 * script count movies where character wedge antilles is present
 */

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).results;
  data.forEach(movie => {
    movie.characters.forEach((character) => {
      if (character.endsWith('18/')) {
        count += 1;
      }
    });
  });
  console.log(count);
});
