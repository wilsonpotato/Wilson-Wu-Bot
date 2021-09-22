import discord
from discord.ext import commands
import traceback
import sys

#error handling cog

class errorHandling(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

#if the command is not valid, sends a message in the channel
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      error = discord.Embed(title='Invalid Command',
                             description='\nThe command you inputed is not valid!',
                             color=discord.Colour.orange())
      error.add_field(name='Valid Commands:', value='\nhelp, quote, penis, dm, everyone, here, hentai, dm2, dm3, suggest, snipe, meme ')

      await ctx.channel.send(embed=error)

    #sends a message to the channel if someone uses the command on a user that doesn't exist
    if isinstance(error, commands.UserNotFound):
      error = discord.Embed(title='Invalid Username',
                             description='\nMake sure it is the actual username of the user you want to dm.',
                             color=discord.Colour.orange())
      error.add_field(name='PS:', value='\n You need to put "" between usernames.')

      await ctx.channel.send(embed=error)

    #tells the user that the command is on cooldown
    if isinstance(error, commands.CommandOnCooldown):

      error = discord.Embed(title='Command on Cooldown',
                             description=f'This command is on cooldown. Please wait {error.retry_after:.2f}s',
                             color=discord.Colour.orange())

      await ctx.channel.send(embed=error)

    #the bot doesn't have perms :c
    if isinstance(error, commands.MissingPermissions):

      error = discord.Embed(title='Missing Permissions',
                             description='Make sure this bot has the right permissions',
                             color=discord.Colour.orange())

      await ctx.channel.send(embed=error)

    #command missing input
    if isinstance(error, commands.MissingRequiredArgument):

      error = discord.Embed(title='Missing Argument',
                             description="Make sure you haven't missed anything",
                             color=discord.Colour.orange())

      await ctx.channel.send(embed=error)

    #Bad argument
    if isinstance(error, commands.BadArgument):
      error = discord.Embed(title='Bad Argument',
                             description="Check if you have the right stuff.",
                             color=discord.Colour.orange())

      await ctx.channel.send(embed=error)
    if isinstance(error, commands.CommandInvokeError):
        error=discord.Embed(title='Dumbass',description='ur idot, ur bot is already loaded', color=discord.Colour.orange())
    else:
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(errorHandling(bot))