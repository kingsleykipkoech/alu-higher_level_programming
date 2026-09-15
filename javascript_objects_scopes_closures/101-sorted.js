#!/usr/bin/node
const dict = require('./101-data').dict;

const sorted = {};
for (const key in dict) {
  const val = dict[key].toString();
  if (sorted[val] === undefined) {
    sorted[val] = [];
  }
  sorted[val].push(key);
}

console.log(sorted);
