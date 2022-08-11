from nextcord.ext import commands
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption
from nextcord.ui import Button, View, Select
import json
from discord_bot.core.classes import Cog_Extension

intents = Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False


class React(Cog_Extension):
    @commands.command()
    async def popcat(self, ctx):
        pic = File("C:\\Users\\yichieh\\OneDrive\\文件\\GitHub\\discord_bot\\resources\\popcat.png")
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))