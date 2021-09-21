import discord
from discord.ext import commands
import random



#Test cog
class game(commands.Cog):
  def __init__(self, bot):
      self.bot = bot


  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def GuessANumber(self, ctx,*, input=int):
      random_number=random.randint(0,10000)
      if(input==random_number):
          await ctx.channel.send('You got it right')
      else:
          await ctx.channel.cend(f'No you idiot. It is {random_number}')


#Setup the cog
def setup(bot):
    bot.add_cog(game(bot))