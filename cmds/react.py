import discord
from discord.ext import commands
import json
from discord_bot.core.classes import Cog_Extension

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

class React(Cog_Extension):
    @commands.command()
    async def popcat(self, ctx):
        pic = discord.File(jdata['popcat'])
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))