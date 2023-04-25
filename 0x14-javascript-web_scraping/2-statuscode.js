#!/usr/bin/node

/**
 * script that displays status code of a get request
 */

const request = require('request');

request(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
