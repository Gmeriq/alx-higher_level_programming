#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(
  `https://swapi-api.alx-tools.com/api/films/${argv[2]}`,
  async (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const data = JSON.parse(body);
    for (const character of data.characters) {
      await request(character, (err, _response, body) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(JSON.parse(body).name);
      });
    }
  }
);
