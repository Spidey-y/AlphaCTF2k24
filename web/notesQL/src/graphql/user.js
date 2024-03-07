const { gql } = require("apollo-server-express");

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    password: String!
  }
  type Query
  type Mutation {
    createUser(name: String!, email: String!, password: String!): User!
    login(email: String!, password: String!): String
  }
`;

module.exports = typeDefs;
