import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import praw

#loads the .env
load_dotenv()

reddit=praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                   client_secret=os.getenv('SECRET'),
                   username=os.getenv('USERNAME'),
                   password=os.getenv('PASSWORD'),
                   user_agent=os.getenv('USER_AGENT'))



class Dm(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  #normal dm
  @commands.command()
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def dm(self, ctx, user: discord.User, *, msg):
    try:
      await user.send(f'{msg}')
      here_embed = discord.Embed(color=discord.Colour.orange())
      here_embed.set_image(url='https://i.ibb.co/QcbYcnD/tfblade.jpg')
      await user.send(embed=here_embed)
      await ctx.channel.send("Success!")
    except:
      await ctx.channel.send('Bruh restricted dms')


  #meme dm
  @commands.command()
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def dm2(self, ctx, user: discord.User, *, msg):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.hot(limit=50)

    for submission in top:
      all_subs.append(submission)

    if submission.is_self:
      await ctx.channel.send('Type the command again.')
      return
    else:
      random_sub = random.choice(all_subs)
      name = random_sub.title
      url = random_sub.url

      henta = discord.Embed(title=name, color=discord.Colour.orange())
      henta.set_image(url=url)
      try:
        await user.send(f'{msg}')
        await user.send(embed=henta)
        await ctx.channel.send("Success!")
      except:
        await ctx.channel.send('Bruh restricted dms.')



def setup(bot):
    bot.add_cog(Dm(bot))