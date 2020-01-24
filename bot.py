import discord
import json
import os
from discord.ext import commands
from datetime import datetime

time_format = "%a, %d %b %Y @ %I:%M:%S %p"

with open('./config/auth.json', 'r') as a:
    auth = json.load(a)

with open('./config/config.json', 'r') as c:
    config = json.load(c)

client = commands.Bot(
    command_prefix = config["prefix"],
    help_command = commands.DefaultHelpCommand(command_attrs=dict(brief="Displays this message.", description=f"Displays list of commands."), no_category='Utility')
    )

# Client on_ready event/startup event
@client.event
async def on_ready():
    now = datetime.now()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'for {config["prefix"]}help'))
    print(f"Logged in as {client.user} on {len(client.guilds)} servers at {now.strftime(time_format)}")

# Latency command
@client.command(brief="Displays latency.", description="Displays latency.",)
@commands.guild_only()
async def ping(ctx):
    await ctx.send(f"**Latency:** {round(client.latency * 1000)}ms")

# Enable, disable, reload modules
@client.command(brief="Enables a module.", description="Enables a module.")
@commands.guild_only()
async def enable(ctx, extension):
    client.load_extension(f'modules.{extension}')
    print(f"{extension} module was enabled by {ctx.author}.")
    await ctx.send(f"{ctx.author.mention} the `{extension}` module was sucessfully enabled.")

@enable.error
async def enable_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} please enter a valid module name.")

@client.command(brief="Disables a module.", description="Disables a module.")
@commands.guild_only()
async def disable(ctx, extension):
    client.unload_extension(f'modules.{extension}')
    print(f"{extension} module was disabled by {ctx.author}.")
    await ctx.send(f"{ctx.author.mention} the `{extension}` module was sucessfully disabled.")

@disable.error
async def disable_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} please enter a valid module name.")

@client.command(brief="Reloads all modules.", description="Reloads all modules.")
@commands.guild_only()
async def reload(ctx):
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            client.reload_extension(f'modules.{filename[:-3]}')

# Loads all modules on startup
for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        client.load_extension(f'modules.{filename[:-3]}')
        print(f"Module: {filename[:-3]} sucessfully loaded.")

client.run(auth["token"])