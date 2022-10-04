#!/usr/bin/node

// a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;
const currentDict = {};

Object.keys(dict).map(function (key, index) {
  if (currentDict[dict[key]] === undefined) {
    currentDict[dict[key]] = [];
  }
  currentDict[dict[key]].push(key);
});

console.log(currentDict);
