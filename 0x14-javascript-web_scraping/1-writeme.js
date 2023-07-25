#!/usr/bin/node
// importing the fs module
const fs = require('fs');
// setting variables
const filename = process.argv[2];
const data = process.argv[3];

fs.writeFile(filename, data, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
