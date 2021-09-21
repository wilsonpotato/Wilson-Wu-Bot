import discord
from discord.ext import commands
import json
import os

os.chdir("C:\\Users\\Wilson Wu\\PycharmProjects\\wilsonbot")


class storingData(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

#On message
  @commands.Cog.listener()
  async def on_message(self, message):

    #message count
    await adduser(message.author)
    users=await get_msgcount()
    users[str(message.author.id)]["msgcount"] += 1
    with open("msgcount.json", "w") as f:
      users = json.dump(users, f)

  #Suggestions
  @commands.command()
  @commands.cooldown(1,200, commands.BucketType.user)
  async def suggest(self, ctx, msg):
    data=msg
    with open("suggestions.txt", "a") as myfile:
      myfile.write(data)
      myfile.write("\n")
    await ctx.channel.send('Suggestion added!')

 # Tells ppl info
  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def info(self, ctx):
    await adduser(ctx.author)
    users = await get_msgcount()

    embed = discord.Embed(title=f"{ctx.author.name}",
                          colour=discord.Colour.orange())
    embed.set_image(url=ctx.author.avatar_url)
    embed.add_field(name='User ID', value=ctx.author.id, inline=False)
    embed.add_field(name='Number of Messages sent', value=users[str(ctx.author.id)]["msgcount"], inline=False)
    await ctx.channel.send(embed=embed)

 # Leaderboard Command
  @commands.command(aliases=['lb'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def leaderboard(self,ctx, x=10):
    users= await get_msgcount()
    leader_board={}
    total=[]
    for user in users:
      name=int(user)
      total_amount=users[user]["msgcount"]
      leader_board[total_amount]=name
      total.append(total_amount)

    total=sorted(total, reverse=True)

    lb=discord.Embed(title='Leaderboard for Messages Sent', colour=discord.Colour.orange())
    index=1

    for i in total:
      id=leader_board[i]
      member=self.bot.get_user(id)
      name=member.name
      lb.add_field(name=f"{index}.{name}", value=f'{i}', inline=False)
      lb.set_thumbnail(url='https://i.ibb.co/QFwq2hb/Wilson-DIo-1.png')
      if index==x:
        break
      else:
        index+=1
    await ctx.channel.send(embed=lb)



# Opens json file and do stuff
async def adduser(user):
  users=await get_msgcount()

  # loads stuff
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["msgcount"] = 0

  # dumps data
  with open("msgcount.json", "w") as f:
    users = json.dump(users, f)
  return True

async def get_msgcount():
  with open("msgcount.json", "r") as f:
    users = json.load(f)
  return users

def setup(bot):
    bot.add_cog(storingData(bot))