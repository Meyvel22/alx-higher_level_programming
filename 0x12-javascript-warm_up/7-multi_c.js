#!/usr/bin/node

// A script that prints  x times “C is fun”

const myString = process.argv[2];

if (isNaN(Number(myString))) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < myString; x++) {
    console.log('C is fun');
  }
}
