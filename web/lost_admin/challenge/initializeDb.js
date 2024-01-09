const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');

const initializeDb = () => {
    db.serialize(() => {
        db.run(`
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
        )
        `);

        db.run(`
        CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        feedback TEXT
        )
        `);

        console.log('success: db initialized')
    })
};

module.exports = initializeDb