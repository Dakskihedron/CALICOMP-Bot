import discord

from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Change role name
    @commands.command(aliases=['rname'], brief="Changes your role name.", description="Changes your role name.", name="rolename", usage="<newrolename>")
    @commands.guild_only()
    async def role_name(self, ctx, *, name):
        current_name = ctx.author.top_role.name
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            old_name = current_name
            await ctx.author.top_role.edit(name = name)
            await ctx.send(f"{ctx.author.mention} changed your role name from `{old_name}` to `{name}`.")

    @role_name.error
    async def role_name_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(f"{ctx.author.mention} the name must not exceed 100 characters.")

    # Change role colour
    @commands.command(aliases=['rcolour'], brief="Changes your role colour.", description="Changes your role colour.", name="rolecolour", usage="<colourhexcode>")
    @commands.guild_only()
    async def role_colour(self, ctx, colour):
        current_colour = ctx.author.top_role.colour
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            old_colour = current_colour
            colour = colour.replace('#','')
            await ctx.author.top_role.edit(colour = discord.Colour(int(colour, 16)))
            await ctx.send(f"{ctx.author.mention} changed your role colour from `{old_colour}` to `#{colour}`.")

    @role_colour.error
    async def role_colour_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(f"{ctx.author.mention} please enter a valid six character colour hex code.")

def setup(client):
    client.add_cog(Roles(client))