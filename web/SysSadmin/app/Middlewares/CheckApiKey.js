require('dotenv').config();

const apiKey = process.env.API_KEY;

function checkApiKey(req, res, next) {
    const authorizationHeader = req.headers.authorization;

    if (!authorizationHeader) {
        return res.status(401).json({ error: 'Unauthorized - API key required' });
    }

    const suppliedApiKey = authorizationHeader.split('Bearer ')[1];

    if (!suppliedApiKey || suppliedApiKey !== apiKey) {
        return res.status(401).json({ error: 'Unauthorized - Invalid API key' });
    }

    next();
}

module.exports = { checkApiKey };