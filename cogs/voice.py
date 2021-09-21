import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


#Test cog
class voice(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  #Math Help Command
  @commands.group(invoke_without_command=True)
  @commands.cooldown(1, 3, commands.BucketType.user)

  #vc meunu
  async def vc(self, ctx):
      vc_embed=discord.Embed(title="VC Commands", description='Just some commands for VC: w!vc join, w!vc leave, w!vc pause, w!vc resume,',color=discord.Colour.orange())
      vc_embed.set_thumbnail(url="https://i.ibb.co/q75jF6S/image-2021-06-16-115453.png")
      await ctx.channel.send(embed=vc_embed)
      pass

  @vc.command()
  async def join(self, ctx):
      join_embed=discord.Embed(title='Wilson Bot joined VC!', color=discord.Colour.orange())
      channel=ctx.author.voice.channel
      await channel.connect()
      await ctx.channel.send(embed=join_embed)

  @vc.command()
  async def play(self, ctx):
      play_embed=discord.Embed(title='Now playing Rick Roll-Rick', color= discord.Color.orange())
      await ctx.channel.send(embed=play_embed)
      ctx.voice_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe",
                                                   source=r'C:\Users\Wilson Wu\PycharmProjects\wilsonbot\music\ricky.mp3'))

  @vc.command()
  async def pause(self, ctx):
      play_embed = discord.Embed(title='Song paused ', color=discord.Color.orange())
      await ctx.channel.send(embed=play_embed)
      server = ctx.message.guild
      voice_channel = server.voice_client
      voice_channel.pause()

  @vc.command()
  async def resume(self, ctx):
      play_embed = discord.Embed(title='Song will resume.', color=discord.Color.orange())
      await ctx.channel.send(embed=play_embed)
      server = ctx.message.guild
      voice_channel = server.voice_client
      voice_channel.resume()
  @vc.command()
  async def leave(self, ctx):
      play_embed = discord.Embed(title='Bye Bye Onii-chan', color=discord.Color.orange())
      await ctx.channel.send(embed=play_embed)
      await ctx.voice_client.disconnect()


#Setup the cog
def setup(bot):
    bot.add_cog(voice(bot))