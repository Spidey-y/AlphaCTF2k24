const { ObjectId } = require('mongodb');
const jwt = require('jsonwebtoken');
const { connectDB } = require('../database/database');


JWT_SECRET = process.env.JWT_SECRET;
function authenticateToken(req, res, next) {
  const token = req.cookies.token;
  if (!token) return res.redirect('/login');

  jwt.verify(token, JWT_SECRET, async (err, decoded) => {
    if (err) {
      console.error('Token verification error:', err);
      return res.redirect('/login');
    }
    try {
      // Convert the decoded userId to ObjectId
      const db = await connectDB();
      const userId = ObjectId(decoded.userId);
      const collection = db.collection('users');
      const user = await collection.findOne({ _id: userId });
      if (!user) {
        console.log('User not found in the database');
        return res.redirect('/login');
      }

      req.user = user; // Set user data in request for further use in routes
      next();
    } catch (error) {
      console.error('Error verifying user:', error);
      return res.status(500).send('Internal Server Error');
    }
  });
}

module.exports = { authenticateToken };
