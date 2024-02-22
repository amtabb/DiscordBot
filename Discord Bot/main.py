#Standard library files
import discord
import os
#User-created files that are imported
from logging_action import record_log
from zKeep_alive import keep_alive
from discord.ext import commands
#Discord intents
intents = discord.Intents.default()
intents.members = True

#----Deprecated imports stuff but I wanna keep it here in case I forget how to do it again----
  #User-created files but in other directories that are not found along with the main.py
  #import sys
  #sys.path.append("./Experimentals")
  #import on_message_handler
#----Deprecated stuff but I wanna keep it here in case I forget how to do it again----

# currently deprecated due to focus for SQLite implementation for db
# from replit import db

#Personally speaking, I think we should only have one prefix for ume
prefix = "u!","umeko ","ume ","Ume ","Umeko"
bot = commands.Bot(prefix, intents=intents)
bot.remove_command('help')

#Cogs area
bot.load_extension("Cogs.ume_calculator")
bot.load_extension("Cogs.ume_social")
bot.load_extension("Cogs.ume_social_give")
bot.load_extension("Cogs.ume_weather")
bot.load_extension("Cogs.ume_dict")
bot.load_extension("Cogs.ume_helping")
bot.load_extension("Cogs.ume_on_message_handler")
bot.load_extension("Cogs.db_cog_experimental")

# Bot event
@bot.event
async def on_ready():
  activity_string = '{} servers.'.format(len(bot.guilds))
# Setting `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))
# Setting `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
# Setting `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
# Setting `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string))

  print("We have logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    #RESPONSIBLE FOR HANDLING BOT COMMANDS
    await bot.process_commands(message)

#Things that run without need for events
keep_alive()
record_log()

bot.run(os.getenv("TOKEN"))