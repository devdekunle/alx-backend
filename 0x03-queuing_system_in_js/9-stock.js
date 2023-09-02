const express = require('express');
import { createClient } from 'redis'
const client = createClient();
const app = express();
import { promisify } from 'util';

client.on('error', (error) => {
    console.log(error)
})

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5
    }
];

// get a product/stock from database using id
const getItemById = (id) => {
    for (const product of listProducts) {
        if (product.id === id) {
            return product
        }
    }
}
// promisify the redis get method
const redisGet = promisify(client.get).bind(client)

// set a stock in redis database using the itemId
const reserveStockById = (itemId, stock) => {
    const array = listProducts.filter((item) => item.itemId === itemId);
    client.set(array[0].itemId, stock)
};

async function getCurrentReservedStockById(itemId) {
    try {
        const stock = await redisGet(itemId);
        return stock;
    } catch (error) {
        return {"status":"Product not found"};
    }
}

app.get('/list_products/:itemId', (req, res) => {
    const itemId = req.params.itemId
    res.statusCode = 200;
    const stock = getCurrentReservedStockById(itemId);
    res.json(stock)
})

app.get('/list_products', (req, res) => {
    res.statusCode = 200;
    res.json(listProducts)
})

app.listen(1245, () => {
    console.log(`Server running on ${'127.0.0.1'}:${1245}`);
});
