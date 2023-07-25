#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;

    const wedgeFilms = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    const filmnumbers = wedgeFilms.length;
    console.log(filmnumbers);
  }
});
