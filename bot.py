import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='Robert.', intents = intents)

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
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'extension {extension} loaded.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'extension {extension} unloaded.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'extension {extension} reloaded.')


for filenames in os.listdir('./cmds'):
    if filenames.endswith('.py'):
        # 去除副檔名 .py
        bot.load_extension(f'cmds.{filenames[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])