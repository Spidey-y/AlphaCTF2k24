const config = require("config");
const jwt = require("jsonwebtoken");
const { GraphQLError } = require("graphql");

const { User } = require("../models");

const resolvers = {
  Mutation: {
    async createUser(parent, { name, email, password }) {
      return await User.create({ name, email, password });
    },
    async login(parent, { email, password }) {
      const user = await User.findOne({
        where: { email: email, password: password },
      });
      if (!user)
        throw new GraphQLError("Incorrect email or password.", {
          extensions: {
            code: "UNAUTHENTICATED",
          },
        });
      return jwt.sign(
        { id: user.id, email, name: user.name },
        "HAJA-KBIRA-NTA",
        { algorithm: "HS256", subject: "id", expiresIn: "1d" }
      );
    },
  },
};

module.exports = resolvers;
