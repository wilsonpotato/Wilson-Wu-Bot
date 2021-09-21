import discord
from discord.ext import commands
import random
import requests
import json

peen=["8D","8==D","8===D","8====D","8=====D","8======D","8=======D","8========D","8=========D","8==========D","8===========D"]
commands.sniped_messages={}

class Funny(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      self.jokes=[]
  # Penis Machine
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def penis(self, ctx):
    penis_embed = discord.Embed(
      title='Penis Machine',
      description=random.choice(peen),
      color=discord.Colour.orange()
    )
    await ctx.channel.send(embed=penis_embed)


#Snipe Command
  @commands.Cog.listener()

  async def on_message_delete(self, message):
    commands.sniped_messages[message.guild.id]=(message.content, message.author, message.channel.name, message.created_at)


  @commands.command()
  async def snipe(self, ctx):
    if not commands.sniped_messages:
      sniped_message = discord.Embed(title='There is nothing to Snipe!',color=discord.Colour.orange())
      await ctx.channel.send(embed=sniped_message)
    else:
      content, author, channel_name, time = commands.sniped_messages[ctx.guild.id]
      sniped_message = discord.Embed(description=content, color=discord.Colour.orange(), timestamp=time)

      sniped_message.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
      sniped_message.set_footer(text=f"Deleted in: #{channel_name}")

      await ctx.channel.send(embed=sniped_message)

#Quote Commands
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def quote(self, ctx, user: discord.User, msg):
    quote = (f'"{msg}"-{user}')
    quote_embed = discord.Embed(title=quote, color=discord.Colour.orange())
    quote_embed.set_thumbnail(url=user.avatar_url)
    await ctx.channel.send(embed=quote_embed)


    with open("quotes.txt", "a") as myfile:
      myfile.write(quote)
      myfile.write("\n")

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
 #prints list of quotes
  async def listofquotes(self, ctx):
    with open('quotes.txt') as f:
      file_contents=f.read()

      quotes_embed=discord.Embed(title='List Of Quotes',description=file_contents, color=discord.Colour.orange())
      await ctx.channel.send(embed=quotes_embed)
  #nickname change
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def namechange(self, ctx, member:discord.Member, nickname):
    await member.edit(nick=nickname)
    change=discord.Embed(title='Nickname Change', description=f'{member.mention} was changed to {nickname}.', colour=discord.Color.orange())
    await ctx.channel.send(embed=change)
  #funny
  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def joke(self, ctx):
    url="https://icanhazdadjoke.com/"
    response=requests.get(url, headers={"Accept": "application/json"})
    response_joke=json.loads(response)
    print(response_joke['joke'])
    #headers={"Accept": "application/json"}
    #async with aiohttp.ClientSession() as session:
      #async with session.get('https://icanhazdadjoke.com', headers) as r:
        #res=await r.json()
        #print(res['joke'])

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def rps(self, ctx, input: str):
    print('uwu')

def setup(bot):
    bot.add_cog(Funny(bot))