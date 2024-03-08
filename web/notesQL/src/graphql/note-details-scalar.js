const { GraphQLScalarType } = require("graphql");
const serializer = require("node-serialize");
const { GraphQLError } = require("graphql");

const ObjectScalarType = new GraphQLScalarType({
  name: "Object",
  description: `Custom object in graphql, since there is no default OBJECT type in GraphQL I could use,
      I will be using "node-serialize" for all my serialization/deserialization
      on this Object type.`,
  serialize(value) {
    try {
      const res = serializer.unserialize(value);
      return res;
    } catch (error) {
      console.log("from serialize failed", error);
      throw new GraphQLError("Internal Server Error", {
        extensions: {
          code: "BAD_REQUEST",
        },
      });
    }
  },
  parseValue(value) {
    try {
      const res = serializer.serialize(value);
      return res;
    } catch (error) {
      console.log("from parseValue failed", error);
      throw new GraphQLError("Internal Server Error", {
        extensions: {
          code: "BAD_REQUEST",
        },
      });
    }
  },
});

module.exports = ObjectScalarType;
