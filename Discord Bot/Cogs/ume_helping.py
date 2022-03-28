from discord.ext import commands
import discord
import datetime

class help(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  @commands.group()
  async def help(self, ctx):
    embed = discord.Embed(title = "Help", description = "use u!help <command> for more information on a command.", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "Social", value = "inspire, hug, slap, kiss, pet, slots, 8ball, say, Calculator, ud, define, avatar, weather")
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    
    if ctx.invoked_subcommand is None:
      await ctx.send(embed=embed)   

  @help.command()
  async def inspire(self, ctx):
    embed = discord.Embed(title = "inspire", description = "get a quote of inspiration!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!inspire")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)   


  @help.command()
  async def hug(self, ctx):
    embed = discord.Embed(title = "hug", description = "give someone a hug and enlighten their day!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!hug <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

  @help.command()
  async def slots(self, ctx):
    embed = discord.Embed(title = "inspire", description = "see if you can get lucky!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!inspire")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 
 
  @help.command()
  async def _8ball(self, ctx):
    embed = discord.Embed(title = "8ball", description = "use the magic 8ball and get an answer to your question!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!8ball <queston>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)  

  @help.command()
  async def kiss(self, ctx):
    embed = discord.Embed(title = "kiss", description = "give someone a kiss!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!kiss <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)   

  @help.command()
  async def slap(self, ctx):
    embed = discord.Embed(title = "kiss", description = "give someone a slap", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!slap <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)   

  @help.command()
  async def pet(self, ctx):
    embed = discord.Embed(title = "kiss", description = "give someone a pet", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!pet <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 

  @help.command()
  async def givecookie(self, ctx):
    embed = discord.Embed(title = "givecookie", description = "give someone a cookie", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!givecookie <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)  

  @help.command()
  async def say(self, ctx):
    embed = discord.Embed(title = "say", description = "make umeko say something!", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!say <response>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 

  @help.command()
  async def ud(self, ctx):
    embed = discord.Embed(title = "ud", description = "get an urban dictionary definition", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!ud <word>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 

  @help.command()
  async def define(self, ctx):
    embed = discord.Embed(title = "define", description = "get a definition of a word", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!define <word>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 


  @help.command()
  async def Calculator(self, ctx):
    embed = discord.Embed(title = "Calculator", description = "trying inputting numbers in to solve things", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!Calculator <add/subtract/multiply/divide> <number> <number>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

  @help.command()
  async def avatar(self, ctx):
    embed = discord.Embed(title = "avatar", description = "see someone's avatar in full", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!avatar <user>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

  @help.command()
  async def weather(self, ctx):
    embed = discord.Embed(title = "weather", description = "get the weather of any city", color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.add_field(name = "command", value = "u!weather <city>")
    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(help(bot))


