const { Model, DataTypes } = require("sequelize");
const sequelize = require("../../database");

class Note extends Model {}

Note.init(
  {
    details: {
      type: DataTypes.JSONB,
    },
  },
  {
    sequelize,
    modelName: "Note",
    tableName: "notes",
  }
);

module.exports = Note;
