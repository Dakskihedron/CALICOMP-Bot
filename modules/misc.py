import discord
import datetime
from discord.ext import commands

time_format = "%a, %d %b %Y @ %I:%M:%S %p"

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Display latency
    @commands.command(brief="Displays latency.", description="Displays latency.",)
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f"**Latency:** {round(self.client.latency * 1000)}ms")

    # Display user info
    @commands.command(aliases=['uinfo', 'whois'], brief="Displays info about a user.", description="Displays info about a user.\nLeave it blank to display info about yourself.", usage="<user>")
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
            return await ctx.send(f"{ctx.author.mention} please enter a valid user.")

def setup(client):
    client.add_cog(Misc(client))