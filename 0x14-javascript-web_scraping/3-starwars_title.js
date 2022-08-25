#!/usr/bin/node
// script that prints the title of a Star Wars movie.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];
request(url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
