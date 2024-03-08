const { gql } = require("apollo-server-express");

const typeDefs = gql`
  type UserWithoutPassword {
    id: ID!
    name: String!
    email: String!
  }

  type Query
  type Mutation {
    createUser(
      name: String!
      email: String!
      password: String!
    ): UserWithoutPassword!
    login(email: String!, password: String!): String
  }
`;

module.exports = typeDefs;
