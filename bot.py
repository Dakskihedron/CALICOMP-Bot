import discord
import json
import os

from discord.ext import commands

with open('./config/auth.json', 'r') as a:
    auth = json.load(a)

with open('./config/config.json', 'r') as c:
    config = json.load(c)

client = commands.Bot(
    command_prefix = config["prefix"],
    help_command = commands.DefaultHelpCommand(command_attrs=dict(brief="Displays this message.", description=f"Displays list of commands."), no_category='About')
    )

# Bot info
@client.command(brief="Displays bot info.", description="Displays bot info.")
@commands.guild_only()
async def info(ctx):
    info = "```asciidoc\n=== CALICOMP Bot ===\nA Discord bot powered by discord.py\nCreated by: Dakskihedron\nSource: https://github.com/Dakskihedron/CALICOMP-Bot\n```"
    await ctx.send(info)

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        client.load_extension(f'modules.{filename[:-3]}')
        print(f"Extension: {filename[:-3]} sucessfully loaded.")
        
client.run(auth["token"])