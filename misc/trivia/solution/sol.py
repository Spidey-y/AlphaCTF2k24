from os import environ
import discord
from time import sleep
import requests
import base64


def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))


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
                sleep(3)
                messages = [message async for message in channel.history(limit=1)]
                # check if message is an embed
                while not messages[0].embeds:
                    messages = [message async for message in channel.history(limit=1)]
                bots_message = messages[0]
                question = bots_message.embeds[0].title
                if "Cypher" in question:
                    cipher = bots_message.embeds[0].description
                    # check if binary or hex or base64
                    if all(c in "01" for c in cipher):
                        answer = ""
                        for i in range(0, len(cipher), 8):
                            answer += chr(int(cipher[i:i+8], 2))
                    elif all(c in "0123456789abcdef" for c in cipher):
                        answer = bytes.fromhex(cipher).decode()
                    else:
                        answer = base64.b64decode(cipher).decode()
                elif "math" in question:
                    x = int(bots_message.embeds[0].description.split(
                        "\n")[0].split("f(")[1].split(")")[0])
                    coefficients = bots_message.embeds[0].description.split(
                        "\n")[1].replace("Equation: f(x) = ", "").split(" + ")
                    coefficients = [int(i.split("x")[0]) for i in coefficients]
                    answer = 0

                    def polynomial(x):
                        result = 0
                        for i, coeff in enumerate(coefficients):
                            result += coeff * (x ** i)
                        return result
                    answer = polynomial(x)
                elif "matrix" in question:
                    matrix = bots_message.embeds[0].description.split("\n")[
                        1:-1]
                    new_matrix = []
                    for row in matrix:
                        new_matrix.append([int(i) for i in row.split(" ")])

                    for i, row in enumerate(new_matrix):
                        for j, val in enumerate(row):
                            if val == 1:
                                answer = f"({i+1},{j+1})"
                else:
                    capacity = int(bots_message.embeds[0].description.split(
                        "\n")[0].split("capacity ")[1].replace("?", ""))
                    items = bots_message.embeds[0].description.split("\n")[1:]
                    new_items = []
                    for item in items:
                        new_items.append((int(item.split(",")[0].split(
                            " ")[-1]), int(item.split(",")[1].split(" ")[-1])))
                    items = new_items
                    answer = str(knapSack(capacity, [w for w, _ in items], [
                                 v for _, v in items], len(items)))

                await channel.send(f"!submit {answer}")
                sleep(2)

    async def on_ready(self) -> None:
        await self.change_presence(activity=discord.Game(name="!solve"))
        await self.tree.sync()
        print(f'{self.user} has connected to Discord!')


if __name__ == "__main__":
    client = Alphabot()
    client.run(
        "OTkxNDQzNTczMzMxNDY4Mzk4.GYvPxq.9j70HybVPmBqyM-JwhlKYZy3lPBvh_Gs0hHgW8")
