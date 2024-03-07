function onlyLocalhost(req, res, next) {
    const ip = req.ip;

    // Check if the IP is either IPv4 or IPv6 localhost
    const isLocalhost = ip === '127.0.0.1' || ip === '::1' || ip === '::ffff:127.0.0.1';

    if (!isLocalhost) {
        return res.status(403).send({ error: "Access denied. This attempt will be reported." });
    }

    next();
}

module.exports = { onlyLocalhost };
