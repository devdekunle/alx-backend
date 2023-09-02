/*
A function that creates a job for each data
*/

const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
     }
     // create jobs in the queue push_notification_code_3
     for (const job of jobs) {
        const queueJob = queue.create('push_notification_code_3', job);

        // when job is created in the queue
        queueJob.on('enqueue', () => {
            console.log(`Notification job created: ${queueJob.id}`);
        });

        // when job is completed
        queueJob.on('complete', () => {
            console.log(`Notification job ${queueJob.id} completed`)
        });

        // when the job failed
        queueJob.on('failed', (err) => {
            console.log(`Notification job ${queueJob.id} failed: ${err}`)
        });

        // monitor the jobs progress
        queueJob.on('progress', (progress) => {
            console.log(`Notification job ${queueJob.id} ${progress}% complete`)
        });

        queueJob.save();
    }
};

module.exports = createPushNotificationsJobs
