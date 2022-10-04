#!/usr/bin/node

// a function that returns the number of occurences in a list.

exports.nbOccurences = function (list, searchElement) {
  let tally = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      tally += 1;
    }
  }
  return tally;
};
