import { createClient, print } from 'redis';

const client = createClient()

client.on('error', error => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.hset('HolbertonSchools', 'Portland', 50, 'Seattle', 80, 'New York', 20, 'Bogota', 20, 'Cali', 40, 'Paris', 2, print);

client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) console.log(err)
    console.log(reply);
});
