import discord
import os

from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Extension commands grouping
    @commands.group(brief="Extension commands group.", description="Extension commands group.", invoke_without_command=True)
    @commands.guild_only()
    @commands.is_owner()
    async def ext(self, ctx):
        await ctx.send(f"{ctx.author.mention} please enter a valid subcommand.")

    # List of extensions
    @ext.command(brief="Displays a list of extensions.", description="Displays list of extensions.", name="list")
    @commands.guild_only()
    @commands.is_owner()
    async def ext_list(self, ctx):
        exts_list = []
        newline = "\n  "
        for filename in os.listdir('./modules'):
            if filename.endswith('.py'):
                exts_list.append(filename[:-3])
        await ctx.send(f"```List of extensions:\n  {newline.join(exts_list)}\n```")

    # Load an extension
    @ext.command(brief="Loads an extension.", description="Loads an extension.", name="load")
    @commands.guild_only()
    @commands.is_owner()
    async def ext_load(self, ctx, extension):
        if extension == "admin":
            return
        else:
            self.client.load_extension(f'modules.{extension}')
            print(f"Extension: {extension} was loaded by {ctx.author}.")
            await ctx.send(f"The `{extension}` extension was sucessfully loaded.")

    # Reload all extensions
    @ext.command(brief="Reloads all extensions.", description="Reloads all extensions.", name="reloadall")
    @commands.guild_only()
    @commands.is_owner()
    async def ext_reload_all(self, ctx):
        for filename in os.listdir('./modules'):
            if filename.endswith('.py'):
                self.client.reload_extension(f'modules.{filename[:-3]}')
                print(f"Extension: {filename[:-3]} was reloaded by {ctx.author}.")
        await ctx.send("Successfully reloaded all extensions.")

    # Unload an extension
    @ext.command(brief="Unloads an extension.", description="Unloads an extension.", name="unload")
    @commands.guild_only()
    @commands.is_owner()
    async def ext_unload(self, ctx, extension):
        if extension == "admin":
            return await ctx.send("The admin extension cannot be unloaded.")
        else:
            self.client.unload_extension(f'modules.{extension}')
            print(f"Extension: {extension} was unloaded by {ctx.author}.")
            await ctx.send(f"The `{extension}` extension was sucessfully unloaded.")

    @ext_load.error
    @ext_unload.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f"{ctx.author.mention} please enter a valid extension name.")

def setup(client):
    client.add_cog(Admin(client))