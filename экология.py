import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def ecology(ctx):
    await ctx.send(f'Береги землю! Выбрасывай мусор в положенные для этого места! А то сам окажешься там засорив планету! ')
    @bot.command()
async def help(ctx):
    await ctx.send(f'введи комнду $hello или $ecology ')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("token")
