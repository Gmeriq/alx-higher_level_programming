#!/usr/bin/node

// Prints a message depending on the arguments passed

const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
