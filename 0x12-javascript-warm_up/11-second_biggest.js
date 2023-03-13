#!/usr/bin/node

// find the second biggest in a list

function secbig (arr) {
  let max = arr[0];
  let sec = arr[0];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      sec = max;
      max = arr[i];
    } else if (arr[i] > sec && arr[i] !== max) {
      sec = arr[i];
    }
  }
  return sec;
}
const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(process.argv[i]);
}
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secbig(arr));
}
