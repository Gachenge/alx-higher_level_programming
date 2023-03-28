#!/usr/bin/node
// imports an array and computes a new one
const list = require('./100-data').list;

const nlist = list.map(myFunction);
function myFunction(value, index, array){
    return value * index;
}
console.log(list);
console.log(nlist);
