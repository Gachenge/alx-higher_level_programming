#!/usr/bin/node

/**
 * script that reads and prints the contents of a File
 */
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) { return console.error(err); }
  console.log(data);
});
