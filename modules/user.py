import discord
from discord.ext import commands
import datetime

time_format = "%a, %d %b %Y @ %I:%M:%S %p"

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Userinfo command
    @commands.command(aliases=['info'], brief="Displays info about a user.", description="Displays info about a user.\nLeave it blank to display info about yourself.")
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

    # Change role name command
    @commands.command(aliases=['rolen'], brief="Changes your role name.", description="Changes your role name.")
    @commands.guild_only()
    async def rolename(self, ctx, *, newrolename):
        curname = ctx.author.top_role.name
        oldname = None
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            oldname = curname
            await ctx.author.top_role.edit(name = newrolename)
            await ctx.send(f"{ctx.author.mention} changed your role name from `{oldname}` to `{newrolename}`.")

    @rolename.error
    async def rolename_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"{ctx.author.mention} 100+ characters: you think you're fucking funny?")

    # Change role colour command
    @commands.command(aliases=['rolec'], brief="Changes your role colour.", description="Changes your role colour.")
    @commands.guild_only()
    async def rolecolour(self, ctx, hexcolourcode):
        curcolour = ctx.author.top_role.colour
        oldcolour = None
        if ctx.author.top_role.position == 0:
            return await ctx.send(f"{ctx.author.mention} your role cannot be changed.")
        else:
            oldcolour = curcolour
            hexcolourcode = hexcolourcode.replace('#','')
            await ctx.author.top_role.edit(colour = discord.Colour(int(hexcolourcode, 16)))
            await ctx.send(f"{ctx.author.mention} changed your role colour from `{oldcolour}` to `{hexcolourcode}`.")
    
    @rolecolour.error
    async def rolecolour_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"{ctx.author.mention} please enter a valid six character hex colour code.")

def setup(client):
    client.add_cog(User(client))