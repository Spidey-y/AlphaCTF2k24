const { Note } = require("../models");
const { GraphQLError } = require("graphql");

const ObjectScalarType = require("./note-details-scalar");

const resolvers = {
  Query: {
    async note(parent, { id }, context) {
      if (Object.keys(context.user).length === 0)
        throw new GraphQLError(
          "You must be authenticated to perform this action.",
          {
            extensions: {
              code: "UNAUTHORIZED",
            },
          }
        );
      return await Note.findOne({ where: { id, UserId: context.user.id } });
    },

    async notesByLoggedInUser(parent, args, context) {
      if (Object.keys(context.user).length === 0)
        throw new GraphQLError(
          "You must be authenticated to perform this action.",
          {
            extensions: {
              code: "UNAUTHORIZED",
            },
          }
        );
      return await Note.findAll({ where: { UserId: context.user.id } });
    },
  },
  Mutation: {
    async createNote(parent, { details }, { user }) {
      if (Object.keys(user).length === 0)
        throw new GraphQLError(
          "You must be authenticated to perform this action.",
          {
            extensions: {
              code: "UNAUTHENTICATED",
            },
          }
        );
      return await Note.create({ details, UserId: user.id });
    },
  },
  Object: ObjectScalarType,
};

module.exports = resolvers;
