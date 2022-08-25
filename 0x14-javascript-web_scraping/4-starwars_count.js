#!/usr/bin/node
// script that prints the number of movies.

const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let counter = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const char in characters) {
        if (characters[char].includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
