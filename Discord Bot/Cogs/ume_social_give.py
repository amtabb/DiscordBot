import discord
from discord.ext import commands
import datetime
import embedlinks
import secrets


# UME SOCIALS GIVE ARE FOR COMMANDS THAT ARE 'GIVABLE'
# Commands such as cookies and possible others
class ume_social_give(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  @commands.group()
  async def give(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.message.channel.send("What should I give?")

  @give.command()
  async def cookie(self, ctx, *, server_member : discord.Member):
    #if none type do nothing
    if server_member is None:
      pass
    
    chosen_image = secrets.SystemRandom().choice(embedlinks.yumcookie)
  
    embed = discord.Embed(description=f"{ctx.author.name} gave a cookie to {server_member.name}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)

#must-have for each cog. load_extension will look for this
def setup(bot):
  bot.add_cog(ume_social_give(bot))
