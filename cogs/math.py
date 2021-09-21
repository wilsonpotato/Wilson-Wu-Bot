import discord
from discord.ext import commands


#Test cog
class math(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  #Math Help Command
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)

  #Math menu
  async def math(self, ctx):
      embed=discord.Embed(title='Math Commands',
                          description="Just some math commands. Don't know why you would use a discord bot instead of a calculator.",
                          colour=discord.Colour.orange())
      embed.set_thumbnail(url='https://i.imgflip.com/4/3s0ukd.jpg')

      #Adds the explanation
      embed.add_field(name='Addition', value='w!add [number] [number2]=[number]+[number2]', inline=False)
      embed.add_field(name='Subtraction', value='w!subtract [number] [number2]=[number]-[number2]', inline=False)
      embed.add_field(name='Multiplication', value='w!multiply [number] [number2]=[number]*[number2]', inline=False)
      embed.add_field(name='Division', value='w!divide [number] [number2]=[number]%[number2]', inline=False)

      #Send the embed in the channel
      await ctx.channel.send(embed=embed)


  #Addition Command
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)

  async def add(self, ctx, left:int, right:int):
      try:
          answer = left + right
          embed = discord.Embed(title='The sum is...', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.', colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)

  #Subtraction Command
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def subtract(self, ctx, left: int, right: int):
      try:
          answer = left - right
          embed = discord.Embed(title='The Difference is...', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.',
                                colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)

  # Multiplication Command
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def multiply(self, ctx, left: int, right: int):
      try:
          answer = left * right
          embed = discord.Embed(title='The product is...', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.',
                                colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)

  #Division Command
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def divide(self, ctx, left: int, right: int):
      try:
          answer = left // right
          embed = discord.Embed(title='The quotient is...', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.',
                                colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
  #sqrt command

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def sqrt(self, ctx, num:int):
      try:
          answer = await math.sqrt(num)
          embed = discord.Embed(title='Budget calculator', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.',
                                colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def factorial(self, ctx, num:float):
      try:
          x=num
          j=1
          i=1

          for i in range(x):
              i+=1
              j=j*i

          answer=j
          embed = discord.Embed(title='The answer is...', description=answer, colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)
      except:
          embed = discord.Embed(title='Invalid Numbers', description='Please use valid numbers.',
                                colour=discord.Colour.orange())
          await ctx.channel.send(embed=embed)





#Setup the cog
def setup(bot):
    bot.add_cog(math(bot))