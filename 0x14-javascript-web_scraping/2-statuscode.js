#!/usr/bin/node
// getting requests
const request = require('request');

// url to pass
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
