from nextcord.ext import commands
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption
from nextcord.ui import Button, View, Select
from discord_bot.core.classes import Cog_Extension

intents = Intents.default()
intents.message_content = True
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