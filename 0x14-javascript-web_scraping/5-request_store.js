#!/usr/bin/node

/**
 * script to get contents of a webpage and stores it in a file
 */

const fs = require('fs');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
