const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');
require('dotenv').config()

const express = require('express');
const app = express();
const port = 1337;
app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

const initializeDb = require('./initializeDb')


app.post('/feedback', (req, res) => {
    const { feedback } = req.body;
    const insertUserQuery = `INSERT INTO feedbacks (feedback) VALUES ('${feedback}')`;

    db.exec(insertUserQuery, (err) => {
        if (err) {
            res.render('./feedback', { error: 'internal error happned' + err, msg: '' })
        }
        else {
            res.render('./feedback', { msg: 'feedback sent successfully', error: '' })
        }
    });

});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    try {
        const sqlQuery = 'SELECT * FROM users WHERE username = ? ';
        db.get(sqlQuery, [username], (err, row) => {
            if (err) {
                console.log('error happened')
                return res.render('./login', { error: `internal error try again`, msg: '' });
            }
            if (!row) {
                return res.render('./login', { error: 'Authentication failed', msg: '' });
            }
            if (row.password === password) {
                res.send(process.env.FLAG);
            }
            else {
                return res.render('./login', { error: 'Authentication failed', msg: '' });
            }
        });
    } catch (error) {
        res.render('./login', { error: 'Authentication failed', msg: `${sqlQuery}` });
    }

});


app.get('/', (req, res) => {
    res.render('./index')
});
app.get('/login', (req, res) => {
    res.render('./login', { msg: '', error: '' })
});
app.get('/feedback', (req, res) => {
    res.render('./feedback', { msg: '', error: '' })
});


initializeDb()
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
