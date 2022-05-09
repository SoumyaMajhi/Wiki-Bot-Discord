import discord
import os
# import requests
# import json
# import random
from keep_alive import keep_alive
import wikipedia


bot = discord.Client()

#bot.remove_command("help")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot)) #shows an opening line in console
  await bot.change_presence(activity=discord.Game(name="with Millions of Articles"))

def wiki_summary(arg):
  definition = wikipedia.summary(arg, chars = 2048,auto_suggest=True, redirect=True)
  return definition
  
  #sentences=3, chars=1000,

@bot.event
async def on_message(message):
  msg = message.content #for shortening
  words = msg.split("$search",1)[1]

  if msg.startswith("$search"):
    words = msg.split("$search",1)[1]
    search = discord.Embed(title = wikipedia.page(words).title, description = wiki_summary(words), colour = discord.Colour.purple())
    await message.channel.send(content=None, embed=search)

  



keep_alive()

bot.run(os.getenv('TOKEN'))
