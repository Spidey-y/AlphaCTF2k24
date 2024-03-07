const { gql } = require("apollo-server-express");

const typeDefs = gql`
  scalar Object

  type Note {
    id: ID!
    details: Object!
  }

  extend type Query {
    note(id: ID!): Note
    notesByLoggedInUser: [Note!]
  }

  extend type Mutation {
    createNote(details: Object!): Note!
  }
`;

module.exports = typeDefs;
