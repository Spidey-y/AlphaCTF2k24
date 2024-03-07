require('dotenv').config();

const apiKey = process.env.API_KEY;

function checkApiKey(req, res, next) {
    const suppliedApiKey = req.headers.authorization.split('Bearer ')[1];
    console.log(suppliedApiKey)
    // Assuming the API key is stored without the 'Bearer ' prefix in the .env file
    if (!suppliedApiKey || suppliedApiKey !== apiKey) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    next();
}

module.exports = { checkApiKey };
