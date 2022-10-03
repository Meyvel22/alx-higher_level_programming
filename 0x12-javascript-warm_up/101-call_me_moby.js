#!/usr/bin/node

// a function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};
