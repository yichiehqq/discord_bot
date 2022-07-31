import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False


bot = commands.Bot(command_prefix='Robert', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1003186094965264384)
    await channel.send(f'{member} joins!')
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1003186124627390564)
    await channel.send(f'{member} leaves!')
    print(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')
    
bot.run('MTAwMzE3MDI0OTA0ODM0Njc2NQ.GPaUf_._1Zl8be63_kaMpP-jO7KFiSSgFT2UNzAVHQ7VQ')
    

