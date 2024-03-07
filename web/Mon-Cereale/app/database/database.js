const { MongoClient } = require('mongodb');

const uri = 'mongodb://mongo:27019/mon-cereale-database';
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function connectDB() {
  try {
    await client.connect();
    console.log('Connected to MongoDB');
    return client.db('mon-cereale-database');
  } catch (err) {
    console.error('Error connecting to database:', err);
    throw err;
  }
}

module.exports = { connectDB };
