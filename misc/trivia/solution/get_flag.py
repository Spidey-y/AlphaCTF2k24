import discord


class CustomClient(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")
        async for i in self.guilds[0].voice_channels[0].history(limit=10):
            print(i.content)


token = "MTIxMzU4MzgxMTE4NzgzNDk3MA.GarEwu.iUGt_9acezO0JSejmIO5iIvcqPj_vuh2rtqMyg"
client = CustomClient()
client.run(token)
