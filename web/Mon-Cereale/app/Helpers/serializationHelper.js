const serialize = require('node-serialize');

function serializeUserData(userData) {
  return Buffer.from(serialize.serialize(userData)).toString('base64');
}

function deserializeUserData(serializedUserData) {
  console.log(serializeUserData)
  const decoded = Buffer.from(serializedUserData, 'base64').toString();
  console.log(decoded)
  unserialised = serialize.unserialize(decoded)
  return unserialised;
}

module.exports = { serializeUserData, deserializeUserData };
