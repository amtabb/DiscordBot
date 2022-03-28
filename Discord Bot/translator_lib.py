#THIS IS WHERE WE'LL HOLD MOST OF THE METHODS FOR TRANSLATION
import discord
from google.cloud import translate
import json


# Takes in a string that may or may not be a language code.
# If it is a language code, it returns said code.
# If it is a language, it returns the affiliated code. If not, it returns -1
def check_language(code, target):
    with open('languages.json') as data:
        languages = json.load(data)
        for lang in languages:
            if (lang['language'].lower() == code.lower())or (lang['name'].lower() == code.lower()):
                return lang[target]
        return "False"


# Translates the message and returns the output object.
def translate_message(message, target):
    translate_client = translate.Client.from_service_account_json('api-key.json')
    result = translate_client.translate(message, target_language=target)
    return result


def format_response(response):
    language_code = response['detectedSourceLanguage']
    language_name = check_language(language_code, 'name')
    formatted_return = ("```" + "\n" + " \"" + response['translatedText'] + "\"\n" + "```" + "\n" +
                        "**Source Language:** " + language_name + " **|** " + language_code + "\n")
    return formatted_return


def translate_to_en(ctx, bot_obj,last_message_var):
    translation = translate_message(last_message_var, "en")
    formatted_return = format_response(translation)
    return bot_obj.send_message(ctx.channel, formatted_return)






# TRANSLATION BLOCK ---REMOVED FROM MAIN.PY---
"""
@bot.group(name="translate")
async def _translate(ctx):
  global last_sent_message
  if ctx.invoked_subcommand is None:
   await ctx.channel.send("Invalid command for s!translate. Please type **s!translate help** for command")

@_translate.command()
async def help(ctx):
  await ctx.channel.send("Type - **s!translate previous** to translate the message above!!")

@_translate.command()
async def previous(ctx):
  await translator_lib.translate_to_en(ctx, bot,last_sent_message)
"""
# TRANSLATION BLOCK ---REMOVED FROM MAIN.PY---