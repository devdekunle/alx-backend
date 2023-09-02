const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];
const queue = kue.createQueue();
for (const job of jobs) {
    // create a new queue
    const notificationQueue = queue.create('push_notification_code_2', job)
    .attempts(3)
    .backoff(true);

    // if job successfully created
    notificationQueue.on('enqueue', () => {
        console.log(`Notification job created: #${notificationQueue.id}`);
    });

    // on job completion
    notificationQueue.on('complete', () => {
        console.log(`Notification job #${notificationQueue.id} completed`);
    });

    // on job failure
    notificationQueue.on('failed', (err) => {
        console.log(`Notification job #${notificationQueue.id} failed: ${err}`);
    });

    // on progress
    notificationQueue.on('progress', (progress) => {
        console.log(`Notification job #${notificationQueue.id} ${progress}% complete`);
    });
    notificationQueue.save();
}
