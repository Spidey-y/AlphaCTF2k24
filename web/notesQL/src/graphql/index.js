const { mergeTypeDefs, mergeResolvers } = require("@graphql-tools/merge");
const userTypeDefs = require("./user");
const noteTypeDefs = require("./note");
const userResolver = require("./userResolver");
const noteResolver = require("./noteResolver");

const typeDefs = mergeTypeDefs([userTypeDefs, noteTypeDefs]);
const resolvers = mergeResolvers([userResolver, noteResolver]);

module.exports = { typeDefs, resolvers };
