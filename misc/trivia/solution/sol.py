from os import environ
import discord
from time import sleep
import requests


class Alphabot(discord.Client):
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
        if message.content.startswith("!solve"):
            for _ in range(100):
                channel = message.channel
                await channel.send("!trivia")
                sleep(6)
                messages = [message async for message in channel.history(limit=1)]
                bots_message = messages[0]
                question = bots_message.embeds[0].title
                answers = [_.strip().split("  ")[-1]
                           for _ in messages[0].embeds[0].description.split("\n")]
                query = "https://www.google.com/search?q=" + \
                    question.replace(" ", "+")
                response = requests.get(query)
                counts = [response.text.count(answer) for answer in answers]
                answer = answers[counts.index(max(counts))]
                await bots_message.add_reaction("🇦" if answer == answers[0] else "🇧" if answer == answers[1] else "🇨" if answer == answers[2] else "🇩")
                sleep(3)

    async def on_ready(self) -> None:
        await self.change_presence(activity=discord.Game(name="!solve"))
        await self.tree.sync()
        print(f'{self.user} has connected to Discord!')


if __name__ == "__main__":
    client = Alphabot()
    client.run(
        "OTkxNDQzNTczMzMxNDY4Mzk4.GYvPxq.9j70HybVPmBqyM-JwhlKYZy3lPBvh_Gs0hHgW8")
