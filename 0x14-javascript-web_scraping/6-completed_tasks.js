#!/usr/bin/node
/**
 * Write a script that computes the number of tasks completed by user id.
 * Only print users with completed task
 */
const request = require('request');

request(process.argv[2], (err, body) => {
  if (err) {
    console.error(err);
  }
  const respObj = JSON.parse(body.body);

  const tasksCompleted = {};
  respObj.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
