import discord
from discord.ext import commands
import random
import praw
import asyncpraw

reddit=asyncpraw.Reddit(client_id="wFV657W4HM2uaw",
                   client_secret="lBq9FEKc-0esigXO92IlyI3rTR9W8g",
                   username="WillyThePotato",
                   password="351386WWW",
                   user_agent="apple")



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