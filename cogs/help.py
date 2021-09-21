import discord
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  # DIY Help Command
  @commands.group(invoke_without_command=True)
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def help(self, ctx):
    help_embed = discord.Embed(
      title='Wilson Bot Help',
      description='\n Hello! I am Wilson Bot and I am worthless! \n Type w!help [category] for commands in that category.',
      color=discord.Colour.orange()
    )
    help_embed.set_thumbnail(url='https://i.ibb.co/QFwq2hb/Wilson-DIo-1.png')
    help_embed.add_field(name='Funny', value='Commands that are funny', inline=False)
    help_embed.add_field(name='Mention', value='Commands that mentions people', inline=False)
    help_embed.add_field(name='Dm', value='Commands that dms people', inline=False)
    help_embed.add_field(name='Reddit', value='Reddit Commands', inline=False)
    help_embed.add_field(name='Other', value='Other random Commands', inline=False)

    await ctx.channel.send(embed=help_embed)
    pass

  @help.command()
  # funny commands
  async def Funny(self, ctx):
      embed = discord.Embed(title='Funny Commands',
                            description='w!penis, w!snipe, w!quote [user] [message] \n w!listofquotes')
      await ctx.channel.send(embed=embed)


  @help.command()
  # Reddit commands
  async def Reddit(self,ctx):
      embed = discord.Embed(title='Reddit Commands', description='w!meme')
      await ctx.channel.send(embed=embed)

  @help.command()
  # Reddit commands
  async def Dm(self,ctx):
      embed = discord.Embed(title='Dm Commands',
                            description='w!dm [user] [msg], w!dm2 [user] [msg]')
      await ctx.channel.send(embed=embed)

  @help.command()
  # Reddit commands
  async def Other(self, ctx):
      embed = discord.Embed(title='Other Commands', description='w!suggest [suggestion], w!math')
      await ctx.channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))