import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='Robert', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    welcome_channel_id = int(jdata['welcome_channel'])
    channel = bot.get_channel(welcome_channel_id)
    await channel.send(f'{member} joins!')
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    leave_channel_id = int(jdata['leave_channel'])
    channel = bot.get_channel(leave_channel_id)
    await channel.send(f'{member} leaves!')
    print(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')
    
bot.run(jdata['TOKEN'])
    

