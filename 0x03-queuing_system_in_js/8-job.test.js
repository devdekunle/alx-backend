const kue = require('kue');
const chai = require('chai');
const { expect } = chai;

// Import your function
const createPushNotificationsJobs = require('./8-job');

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    // Enable test mode and prevent job processing
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode after tests are done
    queue.testMode.clear();
    queue.testMode.exit();
  });

  afterEach(() => {
    // Clear the queue between test cases
    queue.testMode.clear();
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check if the correct number of jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should trigger job events correctly', () => {
    const jobs = [
      { phoneNumber: '1111111111', message: 'Test message A' },
      { phoneNumber: '2222222222', message: 'Test message B' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check if job enqueue events were triggered
    expect(queue.testMode.events['enqueue']).to.have.lengthOf(2);

    // Check if job complete events were triggered
    expect(queue.testMode.events['complete']).to.have.lengthOf(2);

    // Check if job failed events were not triggered
    expect(queue.testMode.events['failed']).to.be.undefined;

    // Check if job progress events were triggered
    expect(queue.testMode.events['progress']).to.have.lengthOf(2);
  });
});

