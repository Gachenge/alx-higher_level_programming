#!/usr/bin/node

// convert to integer

const myVar = Math.floor(process.argv[2]);
if (!myVar) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myVar}`);
}
