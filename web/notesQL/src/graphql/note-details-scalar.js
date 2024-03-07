const { GraphQLScalarType } = require("graphql");
const { Kind } = require("graphql/language");
const serializer = require("node-serialize");

const ObjectScalarType = new GraphQLScalarType({
  name: "Object",
  description:
    "Custom object in graphql word since there is no default OBJECT type in GraphQL",
  serialize(value) {
    const res = serializer.unserialize(value);
    return res;
  },
  parseValue(value) {
    const res = serializer.serialize(value);
    return res;
  },
});

module.exports = ObjectScalarType;
