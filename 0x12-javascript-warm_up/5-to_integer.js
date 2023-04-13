#!/opt/homebrew/bin/node

// Converts arguments to numbers

const argv = process.argv;

const num = Number(argv[2]);
if (Number.isInteger(num) === true) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
