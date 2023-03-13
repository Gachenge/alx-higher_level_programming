#!/usr/bin/node

// find the second biggest in a list

function secbig (arr) {
  let myVar = arr[0];
  let yoVar = myVar;
  for (let i = 0; i < arr.length; i++) {
    if (myVar < arr[i]) {
      yoVar = myVar;
      myVar = arr[i];
    } else if (arr[i] > yoVar && arr[i] !== myVar) {
      yoVar = arr[i];
    }
  }
  return yoVar;
}
const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(process.argv[i]);
}
if (arr.length === 0) {
  console.log('0');
} else if (arr.length === 1) {
  console.log('0');
} else {
  console.log(secbig(arr));
}
