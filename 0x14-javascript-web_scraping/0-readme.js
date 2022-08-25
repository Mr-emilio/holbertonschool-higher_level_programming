#!/usr/bin/node
// script that reads and prints the content of a file.

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', function (err, data) {
  console.log(err || data);
});
