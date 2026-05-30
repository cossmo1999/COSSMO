import discord
from discord.ext import commands
import os

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"{bot.user} تم تشغيل")

@bot.command()
async def سلام(ctx):
    await ctx.send("وعليكم السلام!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

TOKEN = os.getenv("bot tokin")

bot.run(TOKIN)