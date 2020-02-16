import discord

from discord.ext import commands
from utils import default

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
        user = user or ctx.author
        embed = discord.Embed(
            title = f"**{user}**",
            colour = user.colour
        )
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Current display name", value=user.display_name, inline=False)
        embed.add_field(name="Joined Discord", value=default.date(user.created_at), inline=False)
        embed.add_field(name="Joined server", value=default.date(user.joined_at), inline=False)
        embed.add_field(name="Highest role in server", value=user.top_role.mention, inline=False)

        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            return await ctx.send(f"{ctx.author.mention} please enter a valid user.")

def setup(client):
    client.add_cog(Misc(client))