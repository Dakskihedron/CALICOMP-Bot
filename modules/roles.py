import discord
import datetime
from discord.ext import commands

time_format = "%a, %d %b %Y @ %I:%M:%S %p"

class User(commands.Cog):
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
            await ctx.send(f"{ctx.author.mention} the name must not exceed 100 characters.")

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
            await ctx.send(f"{ctx.author.mention} changed your role colour from `{oldcolour}` to `{colour}`.")

    # Display user info
    @commands.command(aliases=['uinfo'], brief="Displays info about a user.", description="Displays info about a user.\nLeave it blank to display info about yourself.", usage="<optional:user>")
    @commands.guild_only()
    async def userinfo(self, ctx, user: discord.Member=None):
        if not user:
            embed = discord.Embed(
                title = f"**{ctx.author}**",
                colour = ctx.author.colour
            )
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="Current display name", value=ctx.author.display_name, inline=False)
            embed.add_field(name="Joined Discord", value=ctx.author.created_at.strftime(time_format), inline=False)
            embed.add_field(name="Joined server", value=ctx.author.joined_at.strftime(time_format), inline=False)
            embed.add_field(name="Highest role in server", value=ctx.author.top_role.mention, inline=False)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f"**{user}**",
                colour = user.colour
            )
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="Current display name", value=user.display_name, inline=False)
            embed.add_field(name="Joined Discord", value=user.created_at.strftime(time_format), inline=False)
            embed.add_field(name="Joined server", value=user.joined_at.strftime(time_format), inline=False)
            embed.add_field(name="Highest role in server", value=user.top_role.mention, inline=False)

            await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{ctx.author.mention} please enter a valid user.")

    @rolecolour.error
    async def rolecolour_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"{ctx.author.mention} please enter a valid six character colour hex code.")

def setup(client):
    client.add_cog(User(client))