#!/usr/bin/node
/**
 * prints the number of arguments and the value
 */
let count = 0;
exports.logMe = function (item){ console.log(`${count++}: ${item}`); };
