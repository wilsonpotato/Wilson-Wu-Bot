import discord
from discord.ext import commands
import random
import praw
import asyncpraw
from dotenv import load_dotenv
import os
#loads the .env
load_dotenv()

reddit=praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                   client_secret=os.getenv('SECRET'),
                   username=os.getenv('USERNAME'),
                   password=os.getenv('PASSWORD'),
                   user_agent=os.getenv('USER_AGENT'))



class redditcommands(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  #meme
  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def meme(self, ctx):
    subreddit = await reddit.subreddit("memes")
    all_subs = []
    top = subreddit.hot(limit=50)

    async for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url


    henta = discord.Embed(title=name, color=discord.Colour.orange())
    henta.set_image(url=url)


    await ctx.channel.send(embed=henta)
    return






def setup(bot):
    bot.add_cog(redditcommands(bot))