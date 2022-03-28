from discord.ext import commands

class db_Test(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  @commands.group()
  async def db(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.channel.send("No Subcommand was found/invoked")
    
  
  @db.command()
  async def add(self, ctx):
    await ctx.channel.send("add working")

  @db.command()
  async def edit(self, ctx):
    await ctx.channel.send("edit working")

  @db.command()
  async def delete(self, ctx):
    await ctx.channel.send("delete working")

  @db.command()
  async def select(self, ctx):
    await ctx.channel.send("select working")
  

#must-have for each cog. load_extension will look for this
def setup(bot):
  bot.add_cog(db_Test(bot))