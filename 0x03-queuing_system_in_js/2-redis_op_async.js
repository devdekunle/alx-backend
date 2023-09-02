import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// promisify the client.get method
const asyncGet = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
};

async function displaySchoolValue (schoolName) {
    try {
        const value= await asyncGet(schoolName);
        console.log(value);
    } catch (error) {
        console.log(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
