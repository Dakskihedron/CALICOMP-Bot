import discord
import os

from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # List of extensions
    @commands.command(brief="Displays list of extensions.", description="Displays list of extensions.")
    @commands.guild_only()
    @commands.is_owner()
    async def extlist(self, ctx):
        extlist = []
        nl = "\n  "
        for filename in os.listdir('./modules'):
            if filename.endswith('.py'):
                extlist.append(filename[:-3])
        await ctx.send(f"```List of extensions:\n  {nl.join(extlist)}\n```")

    # Load an extension
    @commands.command(brief="Loads an extension.", description="Loads an extension.")
    @commands.guild_only()
    @commands.is_owner()
    async def load(self, ctx, extension):
        if extension == "admin":
            return
        else:
            self.client.load_extension(f'modules.{extension}')
            print(f"{extension} extension was loaded by {ctx.author}.")
            await ctx.send(f"The `{extension}` extension was sucessfully loaded.")

    # Reload all extensions
    @commands.command(brief="Reloads all extensions.", description="Reloads all extensions.")
    @commands.guild_only()
    @commands.is_owner()
    async def reloadall(self, ctx):
        for filename in os.listdir('./modules'):
            if filename.endswith('.py'):
                self.client.reload_extension(f'modules.{filename[:-3]}')

    # Unload an extension
    @commands.command(brief="Unloads an extension.", description="Unloads an extension.")
    @commands.guild_only()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        if extension == "admin":
            return await ctx.send("The admin extension cannot be unloaded.")
        else:
            self.client.unload_extension(f'modules.{extension}')
            print(f"{extension} extension was unloaded by {ctx.author}.")
            await ctx.send(f"The `{extension}` extension was sucessfully unloaded.")

    @load.error
    @unload.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f"{ctx.author.mention} please enter a valid extension name.")

def setup(client):
    client.add_cog(Admin(client))