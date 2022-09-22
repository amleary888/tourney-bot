import discord
import os
import challonge
import sqlite3

conn = sqlite3.connect()

challonge.set_credentials("L_eary", os.getenv('CHALLONGE'))

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')

        if message.author != self.user:

            if message.content.startswith(".$"):
                if message.content.split(" ")[1] == "hi":
                    await message.channel.send("Hello!")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
