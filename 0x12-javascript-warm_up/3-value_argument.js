#!/usr/bin/node

// print the first argument passed to it

const arg = process.argv[2];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
