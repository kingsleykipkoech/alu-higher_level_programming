#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (completed[todo.userId]) {
          completed[todo.userId]++;
        } else {
          completed[todo.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
