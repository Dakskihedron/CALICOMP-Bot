import discord

from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Change role name
    @commands.command(aliases=['rname'], brief="Changes your role name.", description="Changes your role name.", usage="<newrolename>")
    @commands.guild_only()
    async def rolename(self, ctx, *, name):
        curname = ctx.author.top_role.name
        oldname = None
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            oldname = curname
            await ctx.author.top_role.edit(name = name)
            await ctx.send(f"{ctx.author.mention} changed your role name from `{oldname}` to `{name}`.")

    @rolename.error
    async def rolename_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(f"{ctx.author.mention} the name must not exceed 100 characters.")

    # Change role colour
    @commands.command(aliases=['rcolour'], brief="Changes your role colour.", description="Changes your role colour.", usage="<colourhexcode>")
    @commands.guild_only()
    async def rolecolour(self, ctx, colour):
        curcolour = ctx.author.top_role.colour
        oldcolour = None
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            oldcolour = curcolour
            colour = colour.replace('#','')
            await ctx.author.top_role.edit(colour = discord.Colour(int(colour, 16)))
            await ctx.send(f"{ctx.author.mention} changed your role colour from `{oldcolour}` to `#{colour}`.")

    @rolecolour.error
    async def rolecolour_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(f"{ctx.author.mention} please enter a valid six character colour hex code.")

def setup(client):
    client.add_cog(Roles(client))