#!/usr/bin/node
/**
 * script computed number of tasks completes by user id
 */

const request = require('request');

const task = {};

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);

  data.forEach(element => {
    if (element.completed) {
      const userId = element.userId;
      if (userId in task) {
        task[userId]++;
      } else {
        task[userId] = 1;
      }
    }
  });
  console.log(task);
});
