const { Note } = require("../models");
const ObjectScalarType = require("./note-details-scalar");

const resolvers = {
  Query: {
    async note(parent, { id }, context) {
      return await Note.findOne({ where: { id, UserId: context.user.id } });
    },

    async notesByLoggedInUser(parent, args, context) {
      return await Note.findAll({ where: { UserId: context.user.id } });
    },
  },
  Mutation: {
    async createNote(parent, { details }) {
      return await Note.create({ details });
    },
  },
  Object: ObjectScalarType,
};

module.exports = resolvers;
