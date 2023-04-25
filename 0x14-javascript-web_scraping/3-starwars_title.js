#!/usr/bin/node

/**
 * prints the title of a start wars movie whose episode number
 * matches a given integer
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).title;
  console.log(data);
});
