import discord
import json
import os
import requests
import random
from random import choice
from discord.ext import commands
import aiohttp
import giphy_client 
import time
from giphy_client.rest import ApiException
from pprint import pprint
from keep_alive import keep_alive

client=discord.Client()
bot=commands.Bot(command_prefix="!")


songs=['tu jaane na','agar tum sath ho','tujhe bhula dia','i wish it was me']
sad_words=["sad",'cry',"depress",'depressed','depression','cri']
response_sad=['Cheer Up, Bestie. I love you',
          "Everything's gonna be fine, Bestie. *hugs*",
          "look, ilysm and I'm proud of you <3",
          "Cheer up, the worst is yet to come.",
          "You want a hug, Bestie? :(( ily *tight hug*",
          "If I were a hooman, I would've hugged you to death :(((",
          "Don't be sad pls Bestie Everything gonna Fall back into Place <333"]

def get_quote():
  response=requests.get('https://zenquotes.io/api/random')
  data=json.loads(response.text)
  quote=data[0]['q'] + "  - " + data[0]['a']
    
  return quote


def pickup_line():
  response=requests.get('https://getpickuplines.herokuapp.com/lines/random')
  data=json.loads(response.text)
  line=data['line']
  return line


def insult():
  response=requests.get('https://evilinsult.com/generate_insult.php?lang=en&amp;type=json')
  data=response.text
  return data


def truth():
  response=requests.get('https://api.truthordarebot.xyz/v1/truth?rating=pg13')
  data=json.loads(response.text)
  line=data["question"]
  return line


def dare():
  response=requests.get('https://api.truthordarebot.xyz/v1/dare?rating=pg13')
  data=json.loads(response.text)
  line=data["question"]
  return line


def would_you_rather():
  response=requests.get('https://api.truthordarebot.xyz/v1/wyr?rating=pg13')
  data=json.loads(response.text)
  line=data["question"]
  return line


def never_have_i():
  response=requests.get('https://api.truthordarebot.xyz/v1/nhie?rating=pg13')
  data=json.loads(response.text)
  line=data["question"]
  return line


def paranoia():
  response=requests.get('https://api.truthordarebot.xyz/v1/paranoia?rating=pg13')
  data=json.loads(response.text)
  line=data["question"]
  return line


def truthx():
  response=requests.get('https://api.truthordarebot.xyz/v1/truth?rating=r')
  data=json.loads(response.text)
  line=data["question"]
  return line


def darex():
  response=requests.get('https://api.truthordarebot.xyz/v1/dare?rating=r')
  data=json.loads(response.text)
  line=data["question"]
  return line


def would_you_ratherx():
  response=requests.get('https://api.truthordarebot.xyz/v1/wyr?rating=r')
  data=json.loads(response.text)
  line=data["question"]
  return line

def never_have_ix():
  response=requests.get('https://api.truthordarebot.xyz/v1/nhie?rating=r')
  data=json.loads(response.text)
  line=data["question"]
  return line

def paranoiax():
  response=requests.get('https://api.truthordarebot.xyz/v1/paranoia?rating=r')
  data=json.loads(response.text)
  line=data["question"]
  return line

  
@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))



@client.event
async def on_message(message):
  msg=message.content.lower()
  if message.author==client.user:
    return
  if msg.startswith("prx ily"):
    await message.channel.send(message.author.mention+" ilym ilym muah <3")
    
  if msg.startswith("ihy"):
    await message.channel.send("too kewl to be hated <3")

  
  if msg.startswith('zainab'):
    await message.channel.send("is sahar's Jaan")

  
  if msg.startswith('marry me'):
    if str(message.author)=="P R X#5546":
      await message.channel.send('nikal tu bsdk')
    else:
      await message.channel.send("nfewbjkfwhwefnh ALL YOURSS "+message.author.mention)

  if msg==("ak"):
    await message.channel.send('OMG OMG AK AK MY ONLY TRUE LOVE')
    
  if msg.startswith("who asked"):
    await message.channel.send(message.author.mention + ' ur mom.')

  if msg.startswith("Poocha"):
    await message.channel.send(message.author.mention + ' teri mummy ne')
    
  if msg.startswith("sah@r"):
    await message.channel.send('BHABI BHABI BHABI')
     
  if msg.startswith("hiba"):
    await message.channel.send('IS THE BEST PERSON ON THIS PLANET <3')
    
  if msg.startswith("AA knjr"):
    await message.channel.send(message.author.mention+ ' TERI MA DA KHASAM')

  if message.content.lower() == "prx quote":
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(response_sad))

  if msg.startswith('!best'):
    if str(message.author)=='Henny#2843' or str(message.author)=='suz#0420':
      await message.channel.send(' ur mom ')
    else:
      await message.channel.send(message.author.mention+" The Best obv <33")

  if message.content.lower() == "prx downbad":
    line=pickup_line()
    await message.channel.send(message.author.mention +"  "+ str(line))
    
  if message.content.lower() == "prx mean":
    line=insult()
    await message.channel.send(message.author.mention +"  "+ str(line))

  if message.content.lower() == "sahar":
    await message.channel.send("is Zainab's Jaan")

  if message.content.lower() == "prx truth":
    line=truth()
    await message.channel.send(message.author.mention +"  "+ str(line))

  if message.content.lower() == "prx dare":
    line=dare()
    await message.channel.send(message.author.mention +"  "+ str(line))

  
  if message.content.lower() == "prx never":
    line=never_have_i()
    await message.channel.send(message.author.mention +"  "+ str(line))

  
  if message.content.lower() == "prx wyr":
    line=would_you_rather()
    await message.channel.send(message.author.mention +"  "+ str(line))

    
  if message.content.lower() == "prx paranoia":
    line=paranoia()
    await message.channel.send(message.author.mention +"  "+ str(line))

  
  if message.content.lower() == "xxx truth":
    line=truthx()
    await message.channel.send(message.author.mention +"  "+ str(line))


  
  if message.content.lower() == "xxx dare":
    if str(message.author)=="P R X#5546":
      await message.channel.send(message.author.mention +"  "+random.choice(dares))
    else:
      await message.channel.send(message.author.mention +"  "+random.choice(darez))     
    #line=darex()
    #await message.channel.send(message.author.mention +"  "+ str(line))


  if message.content.lower() == "xxx never":
    line=never_have_ix()
    await message.channel.send(message.author.mention +"  "+ str(line))


  if message.content.lower() == "xxx wyr":
    line=would_you_ratherx()
    await message.channel.send(message.author.mention +"  "+ str(line))

    
  if message.content.lower() == "xxx paranoia":
    line=paranoiax()
    await message.channel.send(message.author.mention +"  "+ str(line))


keep_alive()
string token=''
client.run(os.environ[token])
