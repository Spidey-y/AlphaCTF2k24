const express = require("express");
const { ApolloServer } = require("apollo-server-express");
const graphql = require("./src/graphql");
const { expressjwt } = require("express-jwt");

const bodyParser = require("body-parser");

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

app.use(bodyParser.json());

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    const user = req.auth || {};
    return { user };
  },
  includeStacktraceInErrorResponses: false,
  introspection: true,
  formatError: (formattedError, error) => {
    // Remove stacktrace
    if (formattedError.extensions.code === "BAD_REQUEST") {
      return {
        extensions: {
          code: formattedError.extensions.code,
        },
        message: formattedError.extensions.exception.message,
      };
    }

    return formattedError;
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
