#Setup for Discord bot

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


bot= commands.Bot(command_prefix = "w!", status=discord.Status.online, activity=discord.Game('w!help'),intents=discord.Intents.all())
bot.remove_command("help")


load_dotenv()


extensions=['cogs.Dm', 'cogs.errorHandling', 'cogs.Funny', 'cogs.help', 'cogs.math',  'cogs.redditcommands', 'cogs.storingData', 'cogs.voice', 'cogs.game']
#Shows that the bot is ready
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))



@bot.command()
@commands.is_owner()
async def load(ctx):
  load_embed=discord.Embed(title='Cogs are loaded!', colour=discord.Colour.orange())
  for cog in extensions:
    bot.load_extension(f'{cog}')
    print(f'{cog} is loaded.')
  await ctx.channel.send(embed=load_embed)


@bot.command()
@commands.is_owner()
async def reload(ctx):
  reload_embed = discord.Embed(title='Cogs are reloaded!', colour=discord.Colour.orange())
  for cog in extensions:
    bot.reload_extension(f'{cog}')
    print(f'{cog} is loaded.')
  await ctx.channel.send(embed=reload_embed)



@bot.command()
@commands.is_owner()
async def unload_all(ctx):
  unload_embed = discord.Embed(title='Cogs are unloaded!', colour=discord.Colour.orange())
  for cog in extensions:
    bot.unload_extension(f'{cog}')
    print(f'{cog} is loaded.')
  await ctx.channel.send(embed=unload_embed)

@bot.command()
@commands.is_owner()
async def unload(ctx, cog):
  try:
    cog = cog
    bot.unload_extension(f'{cog}')
    cog_embed=discord.Embed(title=f'{cog} is unloaded', colour=discord.Colour.orange())
    cog_embed.set_thumbnail(url='https://i.ibb.co/QFwq2hb/Wilson-DIo-1.png')
    await ctx.channel.send(embed=cog_embed)
    print(f'{cog} is unloaded.')
  except:
    cog_embed = discord.Embed(title=f'{cog} does not exist.', colour=discord.Colour.orange())
    cog_embed.set_thumbnail(url='https://i.ibb.co/QFwq2hb/Wilson-DIo-1.png')
    await ctx.channel.send(embed=cog_embed)







#Runs bot
bot.run(os.getenv('TOKEN'))