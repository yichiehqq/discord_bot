import discord
from discord.ext import commands
from discord_bot.core.classes import Cog_Extension

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')


def setup(bot):
    bot.add_cog(Main(bot))