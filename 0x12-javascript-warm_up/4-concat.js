#!/usr/bin/node

// Prints arguments in a format

const none = 'undefined';
const argv = process.argv;

if (!argv[2]) {
  console.log(`${none} is ${none}`);
} else if (!argv[3]) {
  console.log(`${argv[2]} is ${none}`);
} else {
  console.log(`${argv[2]} is ${argv[3]}`);
}
