from discord.ext import commands

class on_message_handler(commands.Cog):
  #Constructor to initialize class attributes to an initialized object
  def __init__(self, bot):
    self.bot = bot

  #On ready cog listener that checks for each emoji available in the server
  """
  @commands.Cog.listener()
  async def on_ready(self):
    if len(self.bot.emojis) < 1:
      print("No Emojis Found")
    for emoji in self.bot.emojis:
      print("Emoji ID: "+ str(emoji.id))
      print("Emoji Name: "+ emoji.name)
      print("=================")
  """
  #Cog listens for updates on the on_message event
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return

    msg = message.content
    # message content but as a list and lowered for proper keyword detection
    msg_tolowered = [word_to_lower.lower() for word_to_lower in msg.split(" ")]
    if "uwu" in msg_tolowered:
        await message.channel.send("UwU")

    if "dragon" in msg:
      dragon_id = self.bot.get_emoji(794276815849521152)
      await message.add_reaction("{emoji}".format(emoji = dragon_id))

    #THIS REPORTS THE LAST SENT MESSAGE
    last_sent_message = "" #no value on startup by default
    last_sent_message = message.content
    print("[ {author} ] [From {channel} ]:".format(author = message.author ,channel = message.channel) , last_sent_message)

#must-have for each cog. load_extension will look for this
def setup(bot):
  bot.add_cog(on_message_handler(bot))