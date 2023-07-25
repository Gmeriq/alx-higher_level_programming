#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = JSON.parse(body);
  const taskId = {};

  for (const task of tasks) {
    taskId[task.userId] = 0;
  }
  for (const task of tasks) {
    if (task.completed) {
      taskId[task.userId]++;
    }
  }
  for (const user in taskId) {
    if (taskId[user] === 0) {
      delete taskId[user];
    }
  }

  console.log(taskId);
});
