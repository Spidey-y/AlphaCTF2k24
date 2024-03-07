function isSysAdmin(req, res, next) {
  if (!req.session.user) {
    req.session.user = 'guest';
    console.log(req.session)
  }

  if (req.session.user === 'sysadmin') {
    next();
  } else {
    res.status(401).json({ error: "You're not sysadmin" });
  }
}

module.exports = { isSysAdmin };
