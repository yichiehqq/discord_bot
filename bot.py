from nextcord.ext import commands
from nextcord.abc import GuildChannel
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption
from nextcord.ui import Button, View, Select
import json, os, datetime


intents = Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False



with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    welcome_channel_id = int(jdata['welcome_channel'])
    channel = bot.get_channel(welcome_channel_id)
    await channel.send(f'{member} joins!')
    print(f"{member} joins!")

@bot.event
async def on_member_remove(member):
    leave_channel_id = int(jdata['leave_channel'])
    channel = bot.get_channel(leave_channel_id)
    await channel.send(f'{member} leaves!')
    print(f'{member} leaves!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'extension {extension} loaded.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'extension {extension} unloaded.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'extension {extension} reloaded.')

@bot.slash_command(guild_ids=[int(jdata['guild_id'])])
async def speak(interaction: Interaction, message:str):
    await interaction.response.send_message(f'{message}')


for filenames in os.listdir('./cogs'):
    if filenames.endswith('.py'):
        # 去除副檔名 .py
        bot.load_extension(f'cogs.{filenames[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])