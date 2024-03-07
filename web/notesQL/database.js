const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("gql_notes", "postgres", "postgres", {
  dialect: "postgres", // or whatever database dialect you are using
  host: "localhost",
  sequelizeLogging: false,
});

module.exports = sequelize;
