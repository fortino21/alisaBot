import os

import discord
import random
from dotenv import load_dotenv
from pixivapi import Client,SearchTarget,Sort
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='&')

pixivClient = Client()
pixivClient.login(os.getenv("PIXIV_EMAIL"), os.getenv("PIXIV_PASSWORD"))

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='search',help='Search illustration at pixiv, command : &search <keyword> <number of results>.')
async def search(ctx, keyword, threshold):
    pixivSearchResult = pixivClient.search_illustrations(keyword, search_target= SearchTarget.TITLE_AND_CAPTION , sort=None, duration=None, offset=None)
    illustData = pixivSearchResult['illustrations']
    if len(illustData) == 0 :
        await ctx.send("No result for "+keyword)
    else :
        cnt = 0 
        for v in illustData:
            await ctx.send("https://www.pixiv.net/en/artworks/"+str(v.id))
            if int(threshold) > 0 :
                cnt+=1
                if cnt == int(threshold) :
                    break

bot.run(TOKEN)