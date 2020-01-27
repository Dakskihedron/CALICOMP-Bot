import discord
import json
import os
from discord.ext import commands
from datetime import datetime

with open('./config/auth.json', 'r') as a:
    auth = json.load(a)

with open('./config/config.json', 'r') as c:
    config = json.load(c)

client = commands.Bot(
    command_prefix = config["prefix"],
    help_command = commands.DefaultHelpCommand(command_attrs=dict(brief="Displays this message.", description=f"Displays list of commands."), no_category='Utility')
    )

# Display latency
@client.command(brief="Displays latency.", description="Displays latency.",)
@commands.guild_only()
async def ping(ctx):
    await ctx.send(f"**Latency:** {round(client.latency * 1000)}ms")

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        client.load_extension(f'modules.{filename[:-3]}')
        print(f"Extension: {filename[:-3]} sucessfully loaded.")
        
client.run(auth["token"])