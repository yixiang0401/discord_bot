import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(">> 孤兒過濾機已開啟 <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata['welcome_channel'])
    await channel.send(f"{member} 美麗世界的孤兒加入了!!!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata['leave_channel'])
    await channel.send(f"{member} 可悲的孤兒已離開這個大家庭....")


@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (單位:毫秒)')

@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)

bot.run(jdata['TOKEN'])
