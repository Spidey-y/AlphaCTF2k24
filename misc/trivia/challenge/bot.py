from os import environ
import discord
from cmds import trivia, help, score, submit
from db import create_db, add_server, add_all_servers


TOKEN = environ.get(
    "TOKEN", "token")


class TriviaBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True
        intents.message_content = True
        super().__init__(intents=intents, command_prefix="!")
        self.tree = discord.app_commands.CommandTree(self)

    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return
        if not any(x in message.content for x in ["!submit", "!score", "!trivia", "!help"]):
            return
        if not ("4dmin" in [role.name for role in message.author.roles]):
            await message.channel.send("Only 4dmins can use this bot!")
            return
        if message.content.startswith("!help"):
            await help(message.channel)
        elif message.content.startswith("!score"):
            await score(message.channel, message.guild.id)
        elif message.content.startswith("!trivia"):
            await trivia(message.channel, message.guild.id)
        elif message.content.startswith("!submit"):
            await submit(message.channel, message.guild.id, message.content.split(" ")[1])

    async def on_ready(self) -> None:
        await self.change_presence(activity=discord.Game(name="!help"))
        await self.tree.sync()
        add_all_servers(self)
        print(f'{self.user} has connected to Discord!')

    async def on_guild_join(self, guild):
        add_server(guild.id)


if __name__ == "__main__":
    create_db()
    client = TriviaBot()
    client.run(TOKEN)
