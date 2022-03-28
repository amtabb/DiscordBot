from discord.ext import commands

class audio_stream(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  #Cog listens for updates on the on_message event
  @commands.Cog.listener()
  async def on_message(self, message):
    pass #nothing to add yet so it passes every check

  @commands.group()
  async def audio_stream(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.channel.send("pwease chwoose one of the following uwu: \n** s!Calculator add**  <list of numbers> \n")

  
  @audio_stream.command()
  async def add(self, ctx, *, numbers):
    number_list = [number for number in numbers.split(" ")]
    output = 0
    for number in number_list:
      output += int(number)
    
    await ctx.channel.send("Thiws iws the answew: **{0}**".format(output))

#must-have for each cog. load_extension will look for this
def setup(bot):
  bot.add_cog(audio_stream(bot))