#!/usr/bin/node

// a function that converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
  function currentBase (number) {
    return number.toString(base);
  }

  return currentBase;
};
