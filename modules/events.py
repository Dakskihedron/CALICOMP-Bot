import discord
import json

from discord.ext import commands
from datetime import datetime
from utils import default

with open('./config/config.json', 'r') as c:
    config = json.load(c)

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        now = datetime.now()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'for {config["prefix"]}help'))
        print(f"Logged in as {self.client.user} on {len(self.client.guilds)} servers at {default.date(now)}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            return await ctx.send(f"{ctx.author.mention} you do not have the correct permissions to use this command.")

def setup(client):
    client.add_cog(Events(client))