const mongoose = require('mongoose')
require('dotenv').config()
const express = require('express');
const app = express();
const port = 1330;

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

const BLACKLIST = ['where', 'regex', 'options', 'nin', 'ne', 'or', 'and', 'not',
  'nor', 'exists', 'type', 'mod', 'elemMatch', 'size', 'bitsAllSet', 'bitsAnySet', 'bitsAllClear',
  'bitsAnyClear', 'comment', 'explain', 'hint', 'maxScan', 'maxTimeMS', 'max', 'orderby', 'returnKey',
  'showDiskLoc', 'natural', 'meta', 'slice', 'snapshot', 'rename', 'isolated', 'atomic', 'minDistance',
  'maxDistance', 'near', 'nearSphere', 'geoIntersects', 'geoWithin', 'all', 'elemMatch', 'elemMatch', 'meta',
  'size', 'type', 'language', 'search', 'caseSensitive',
  'diacriticSensitive'
]

function validateInput(userInput) {
  userInput = JSON.stringify(userInput);
  for (const word of BLACKLIST) {
    const regex = new RegExp(`${word}`, 'i');
    if (regex.test(userInput)) {
      console.log(word)
      return false;
    }
  }

  return true;
}

(async function () {

  const userSchema = new mongoose.Schema({
    username: String,
    password: String
  })
  try {
    db = mongoose.connect(process.env.DB_URI)
  } catch (error) {
    console.log('error connecting to the database')
  }
  const User = mongoose.model('User', userSchema)
  try {
    let found = await User.findOne({ username: "admin" });
    if (!found) {
      const adminUser = new User({ username: "admin", password: process.env.FLAG })
      adminUser.save()
    }
  } catch (error) {
    console.log('error getting admin user')
  }

  app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    console.log(req.body)
    console.log(username, password)
    if (!validateInput(username) || !validateInput(password)) {
      res.render('./index', { error: 'Malicious input detected', msg: '' });
    } else {
      try {
        console.log(username, password)
        const userFound = await User.findOne({ username, password })
        if (!userFound) {
          return res.render('./index', { error: 'Authentication failed', msg: '' });
        }
        res.render('./home');
      } catch (error) {
        res.render('./index', { error: 'Authentication failed', msg: '' });
      }
    }
  });

  app.get('/', (req, res) => {
    res.render('./index', { error: '', msg: '' })
  });


  app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
  });

})();