#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  let counter = 0;
  const movies = JSON.parse(body).results;

  for (const movie of movies) {
    const characters = movie.characters;
    for (const character of characters) {
      const characterId = String(character).split('/')[5];
      if (characterId === '18') {
        counter++;
      }
    }
  }
  console.log(counter);
});
