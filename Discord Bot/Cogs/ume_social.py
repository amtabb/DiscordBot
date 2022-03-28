import discord
from discord.ext import commands
import random
import json
import requests
import datetime
import embedlinks


class Social(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  #variables for the class
  templist = []


  @commands.Cog.listener(name="on_ready")
  #---- EVENT BLOCKS ARE THE ONLY AREAS WHERE THIS BLOCK WORKS----
  async def event_on_ready(self):

    #constant variable for Hatsuki Guild
    takenGuild = self.bot.get_guild(434554926258061313)

    usr_counter = 0
    bot_usr_counter = 0
    for member in takenGuild.members:
      Social.templist.append(member.name + " #" + str(member.discriminator))

      if member.bot == False:
        usr_counter += 1
      if member.bot == True:
        bot_usr_counter += 1

    if type(takenGuild) is not None:
      print("Members list is alive and well. Has {} Members\nDiscord Users: {}\nBot Users: {}".format(len(Social.templist), usr_counter, bot_usr_counter))
    #---- EVENT BLOCKS ARE THE ONLY AREAS WHERE THIS BLOCK WORKS----


  #get avatar command
  @commands.command()
  async def avatar(self, ctx, avamember : discord.Member=None):
    if avamember == None:
      user_avatar_url = ctx.author.avatar_url
      await ctx.send(user_avatar_url)
      await ctx.send("Use **s!avatar** *<target member>*  to get a different user's avatar ")
    else:
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)


  #on_join and on_leave listeners here


  @commands.Cog.listener(name="on_message")
  async def event_on_message_(self, message):
    if "welcome" in message.content.split(" ", 1)[0].lower():
      heart_id = self.bot.get_emoji(817052517899698177)
      await message.add_reaction("{emoji}".format(emoji = heart_id))

  # slots command
  @commands.command(pass_context = 'True')
  async def slots(self, ctx):
    responses = ["🍋" , "🍊", "🍉", ":seven:", ]
    embed=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(responses) + random.choice(responses) + random.choice(responses), color=0xE4BAA8)
    embed.set_footer(text="You need triple 7's to win.")
    await ctx.send(embed=embed)

  #inspire command
  @commands.command()
  async def inspire(self, ctx):
    quote = Social.get_quote()
    await ctx.channel.send("```"+ quote + "```")

  #say command 
  @commands.command()
  async def say(self, ctx, *, text=''):
    if text == '':
      await ctx.send("air~")
    else:
      await ctx.send(text)
      await ctx.message.delete()


  # Static methods
  #get quote method
  def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)

  def find_user(user_list, string_to_find):
      output = []
      user_list_lowered = [item.lower() for item in user_list]
      string_to_find_lowered = string_to_find.lower()
      index = -1
      for user in user_list_lowered:
          index += 1
          if string_to_find_lowered == user:
              output.append(user_list[index])
              return output
          elif string_to_find_lowered in user:
              output.append(user_list[index])
      return output


  #Static Member list
  # discord_members = 

  # fun/social command(s)
  # 8ball/made short
  @commands.command(aliases=['8ball'])
  async def _8ball(self, ctx):
    chosen_response = random.choice(embedlinks.responses)
  
    embed = discord.Embed(description=f"{(chosen_response)}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)

  #ping
  @commands.command()
  async def ping(self, ctx):
	  await ctx.channel.send("PogChamp")

  #hug command
  @commands.command()
  async def hug(self, ctx, *, user : discord.Member):
    chosen_image = random.choice(embedlinks.hugLinks)
  
    embed = discord.Embed(description=f"{ctx.author.name} has hugged {user.name}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)


  #slap command
  @commands.command()
  async def slap(self, ctx, *, user : discord.Member):
    chosen_image = random.choice(embedlinks.slapLinks)
  
    embed = discord.Embed(description=f"{ctx.author.name} has slapped {user.name}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)

  #pet command
  @commands.command()
  async def pet(self, ctx, *, user : discord.Member):
    chosen_image = random.choice(embedlinks.petLinks)
  
    embed = discord.Embed(description=f"{ctx.author.name} has petted {user.name}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)

  #kiss command
  @commands.command()
  async def kiss(self, ctx, *, user: discord.Member):
    chosen_image = random.choice(embedlinks.kiss_gifs)
    
    embed = discord.Embed(description=f"{ctx.author.name} has kissed {user.name}",color=0xE4BAA8, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f'Requested by: {ctx.author.name}')
    await ctx.send(embed=embed)

    


  

def setup(bot):
    bot.add_cog(Social(bot))
