import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

game_list = ["League of Legends", "Valorant", "Valheim", "Apex Legends", "Tarkov", "Age of Empires", "Halo", "CSGO", "Seige" ]

game_list_five = ["League of Legends", "Valorant", "Valheim", "Tarkov", "Age of Empires", "Halo", "CSGO", "Siege"]

game_list_greater=["In house Val game", "Valheim", "Age of Empires", "Halo"]

coin_sides = ["Heads", "Tails"]

list_one = list(range(1,101))

help_list_plz = "!plz - will suggest a random game according to how many people are in the voice channel \n!flip - will flip a coin \n!100 - will choose a number from 1-100 \n!game - will suggest a random game \n!help - screams for help"

print(random.choice(game_list))

def get_100():
  return(random.choice(list_one))

def get_game():
  return(random.choice(game_list))

def coin_flip():
  return(random.choice(coin_sides))

def get_help():
  return(help_list_plz)

def game_plz(channel:discord.VoiceChannel):
    members = channel.members #finds members connected to the channel
    # channel.members is a list of discord.Member objects
    #return len(members)
    num_of_ppl = len(members)
    
    if num_of_ppl <= 3:
      return(random.choice(game_list))

    elif num_of_ppl <= 5 and num_of_ppl > 3:
      return(random.choice(game_list_five))

    else:
      return(random.choice(game_list_greater))

        # returns amount of members in the channel

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
 
  try:
    voice_channel = message.author.voice.channel

  except: 
    pass

  msg = message.content
  
  
  if msg.startswith('!game'):
    await message.channel.send(get_game())
  
  if msg.startswith('!plz'):
    await message.channel.send(game_plz(voice_channel))


  if msg.startswith('!flip'):
    await message.channel.send(coin_flip())

  if msg.startswith('!100'):
    await message.channel.send(get_100())

  if msg.startswith('!help'):
    await message.channel.send(get_help())


#@client.event

#async def 
#channel = client.get_channel()
#members = channel.members()
#memids = []
#for member in members:
#  meids.append(member.id)
#print(meids)
keep_alive()
client.run(os.environ['token'])

