#!/usr/bin/node

// Prints x times

const argv = process.argv[2];
let i = 0;

if (!isNaN(argv)) {
  while (i < argv) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
