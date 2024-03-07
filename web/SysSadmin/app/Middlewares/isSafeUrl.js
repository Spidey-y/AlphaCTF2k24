function isSafeUrl(req, res, next) {
    const url = req.body.url;
    const blacklist = ['localhost', '127', '0'];
    const whitelist = ['alphactf', 'alphabit'];
    const urlRegex = /^(http:\/\/|https:\/\/).*\..*/; // Regex pattern to match URLs with a dot in the middle

    if (!url || url.trim() === '') {
        return res.status(400).send('URL parameter is missing or empty.');
    }

    if (!url.match(urlRegex)) {
        return res.status(400).send('URL must start with "http://" or "https://" and contain a dot in the middle.');
    }

    try {
        const hostname = url.split('//')[1].split('.')[0];

        if (blacklist.some(forbiddenHostname => hostname.includes(forbiddenHostname))) {
            return res.status(400).send('You filthy hacker.');
        }

        if (!whitelist.includes(hostname)) {
            return res.status(400).send(`Only the following hostnames are allowed: ${whitelist.join(', ')}`);
        }

        next();
    } catch (error) {
        res.status(500).send(`Failed to validate the URL.\nDetails: ${error.message}`);
    }
}

module.exports = { isSafeUrl };
