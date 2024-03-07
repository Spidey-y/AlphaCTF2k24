const express = require("express");
const { ApolloServer } = require("apollo-server-express");
const graphql = require("./src/graphql");
const { expressjwt } = require("express-jwt");

const sequelize = require("./database");

const { typeDefs, resolvers } = graphql;

const app = new express();

app.use(
  expressjwt({
    secret: "HAJA-KBIRA-NTA",
    algorithms: ["HS256"],
    credentialsRequired: false,
  })
);
const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    const user = req.auth || {};
    return { user };
  },
});

(async () => {
  await sequelize.sync();
  await server.start();
  server.applyMiddleware({ app });
  app.listen({ port: 4000 }, () => {
    console.log(
      `🚀 Server ready at http://localhost:4000${server.graphqlPath}`
    );
  });
})();
