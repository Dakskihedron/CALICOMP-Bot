import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Magic eight ball command
    @commands.command(aliases=['8ball'], brief="Seek advice or fortune-telling.", description="Seek advice or fortune-telling. Provide a question.")
    @commands.guild_only()
    async def eightball(self, ctx, question):
        responses = [
            "it is certain",
            "it is decidedly so",
            "without a doubt",
            "yes - definitely",
            "you may rely on it",
            "as I see it, yes",
            "most likely",
            "outlook good",
            "yes",
            "signs point to yes",
            "reply hazy, try again",
            "ask again later",
            "better not tell you now",
            "cannot predict now",
            "concentrate and ask again",
            "don't count on it",
            "my reply is no",
            "my sources say no",
            "outlook not so good",
            "very doubtful"
        ]
        random.shuffle(responses)
        answer = random.choice(responses)
        await ctx.send(f"{ctx.author.mention} {answer}.")

    @eightball.error
    async def eightball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} you did not provide a question.")

    # Dice command
    @commands.command(aliases=['die', 'rng'], brief="Random number generator.", description="Random number generator. Enter a number larger than zero or one.")
    @commands.guild_only()
    async def dice(self, ctx, number : float):
        if (number).is_integer():
            await ctx.send(f"{ctx.author.mention} {random.randrange(1, number)}")
        else:
            return await ctx.send(f"{ctx.author.mention} please enter a whole number.")

    @dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"{ctx.author.mention} please enter a number larger than zero or one.")

    # Decision command
    @commands.command(aliases=['choose', 'choice', 'pick', 'wheel'], brief="Randomly chooses from inputed choices.", description="Randomly chooses from inputed choices. Separate choices with vertical bar.")
    @commands.guild_only()
    async def decide(self, ctx, *, choices : str):
        alist = choices.split("|")
        random.shuffle(alist)
        answer = random.choice(alist)
        await ctx.send(f"{ctx.author.mention} {answer}")

def setup(client):
    client.add_cog(Fun(client))