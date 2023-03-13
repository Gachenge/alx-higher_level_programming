#!/usr/bin/node

// print square pattern

const myVar = Math.floor(process.argv[2]);
let str = '';
if (!myVar) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
      str += 'X';
    }
    str += '\n';
  }
}
console.log(str);
