const kue = require('kue');
const queue = kue.createQueue();

// define job data
const jobData = {phoneNumber: '08086768991', message: "hello Adekunle!"};

// create a queue named push_notification_code
const notificationQueue = queue.create('push_notification_code', jobData)
.priority('high')
.attempts(3)
.backoff(true);
// when job is created without an error
notificationQueue.on('enqueue', () => {
    console.log(`Notification job created: ${notificationQueue.id}`);
});

// when the job is completed
notificationQueue.on('complete', () => {
    console.log('Notification job completed');
});

// when the job failed
notificationQueue.on('failed', () => {
    console.log('Notification job failed');
});

notificationQueue.save();





