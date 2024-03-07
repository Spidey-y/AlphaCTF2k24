const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const { authenticateToken } = require('../Middlewares/authMiddleware');
const { serializeUserData, deserializeUserData } = require('../Helpers/serializationHelper');
require('dotenv').config();
const { connectDB } = require('../database/database')

const JWT_SECRET = process.env.JWT_SECRET;

router.get('/login', (req, res) => {
  res.sendFile('login.html', { root: 'public' });
});

router.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const db = await connectDB();
    const collection = db.collection('users');
    const user = await collection.findOne({ username, password });
    if (user) {
      const userData = {
        username: user.username,
        role: user.role,
        age: user.age,
        favouriteMeal: user.favouriteMeal,
      };
      serializedUserData = serializeUserData(userData);
      const token = jwt.sign({ userId: user._id, encodedData: serializedUserData }, JWT_SECRET);
      res.cookie('token', token);
      res.redirect('/dashboard');
    } else {
      res.status(401).send('Invalid credentials');
    }
  } catch (err) {
    console.error(err);
    res.status(500).send('Internal Server Error');
  }
});


router.get('/dashboard', authenticateToken, async (req, res) => {
  try {
    const token = req.cookies.token;
    const decodedToken = jwt.verify(token, JWT_SECRET);
    const serializedUserData = decodedToken.encodedData;

    if (serializedUserData) {
      const userData = deserializeUserData(serializedUserData);
      res.json({ userData });
    } else {
      res.status(404).json({ error: 'User data not found' });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});


router.get('/', authenticateToken, (req, res) => {
  res.redirect('/dashboard');
});


module.exports = router;
