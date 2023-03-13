#!/usr/bin/node

// print square pattern

const myVar = Math.floor(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Missing size');
}
else {
  for (let i = 0; i < myVar; i++) {
    let row = '';
    for (let j = 0; j < myVar; j++) {
      row += 'X';
    }
    console.log(row);
  }
}