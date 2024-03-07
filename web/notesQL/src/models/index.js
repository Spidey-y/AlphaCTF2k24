const User = require("./user");
const Note = require("./note");

User.hasMany(Note);
Note.belongsTo(User);

module.exports = { User, Note };
