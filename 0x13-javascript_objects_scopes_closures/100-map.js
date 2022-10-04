#!/usr/bin/node

// a script that imports an array and computes a new array

const list = require('./100-data').list;
const currentList = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(currentList);
