import discord
from discord.ext import commands
import aiohttp

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))

@client.command()
async def prx(ctx,q):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Doggo!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed) # Send the embed

client.run(os.environ['token'])
