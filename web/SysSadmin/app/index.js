const express = require('express');
const routes = require('./routes/routes');
const cookieSession = require('cookie-session');
require('dotenv').config();

const app = express();

// Trust only the loopback addresses (127.0.0.1 and ::1)
app.set('trust proxy', ['loopback', 'linklocal', 'uniquelocal']);

app.use(express.static('public'));

app.use(cookieSession({
  name: 'session',
  keys: [process.env.SECRET_KEY]
}));

app.use('/', routes);

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
