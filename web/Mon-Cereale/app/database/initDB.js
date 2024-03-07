const { connectDB } = require('./database');
const { MongoClient } = require('mongodb');
const crypto = require('crypto');

// Function to initialize the database with an admin user
const initializeDatabase = async () => {
  try {
    const db = await connectDB();
    const collection = db.collection('users');

    await collection.deleteMany({});

    // Generate a random hexadecimal password using crypto.randomBytes
    const adminPassword = crypto.randomBytes(10).toString('hex'); // Adjust the length as needed

    await collection.insertOne({
      username: 'admin',
      password: adminPassword,
      role: 'admin',
      age: 2,
      favouriteMeal: 'Cereals'
    });

    console.log('Admin user inserted successfully');
    console.log('Admin password:', adminPassword);
  } catch (err) {
    console.error('Database initialization error:', err);
  }
};

module.exports = { initializeDatabase };
