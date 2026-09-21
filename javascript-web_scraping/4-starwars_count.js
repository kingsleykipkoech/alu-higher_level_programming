#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      if (film.characters.some((charUrl) => charUrl.includes('/18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
