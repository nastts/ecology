import discord
from discord.ext import commands 
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def ecology_mem(ctx):
    img_lst = os.listdir('images')
    with open(f'images/{random.choice(img_lst)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def helping_nature(ctx):
    await ctx.send(f'привет!!! я очень рад, что ты хочешь миру стать лучше')
    await ctx.send(f'самое важное: сортировка мусора. без этого ничего не получится')
    pon = os.listdir('pon')
    with open(f'pon/{random.choice(pon)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'если каждый человек будет сортировать мусор, мир станет в несколько раз чище')
@bot.command()
async def helping(ctx):
    await ctx.send(f'/helping_nature - расскажет, как правильно сортировать мусор')
    await ctx.send(f'/ecology_mem - мемы про переработку мусора')

bot.run('')
