import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('error', error => {
    console.log(`Redis client not connected to the server: ${error}`)
});

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
    console.log(message);
})
subscriber.subscribe('holberton school channel');


