import discord
import os
import asyncio
import random
from discord.ext import commands

#---------------------------------
token = os.environ['token']
#---------------------------------

bot = commands.Bot(command_prefix='!duck.')
client = discord.Client()

bad_words = ["fucker", "stupid", "fucking", "asshole", "shit", "fuck", "dumb", "ass", "nigger", "dick", "but"]

@client.event
async def on_ready():
    print("Started bot as {0.user}".format(client))
    
@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message("Welcome to this server " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    await client.send_message(member.name + " left the server. Fuck you!!!!")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    elif any (word in message.content for word in bad_words):
        await message.channel.send("You motherfucker! Stop fucking around with those bad words asshole!!!!!")
    
    elif message.content == "!duck.info":
        await message.channel.send("Hello! I am B0B. I am a bot that hates violence and swearing. \n Use '!duck.help' to list all my commands.")
    
    elif message.content == "!duck.help":
        await message.channel.send("List of all B0B commands: \n duck = If you want to duck someone. \n slap = Slap someone. \n fight = start a food fight \n challenge = challenge someone to a duel.")
        
    elif message.content.startswith("!duck.duck"):
        name = message.content.split("!duck.duck ",1)[1] 
        await message.channel.send("Fuck you " + name + "!!!!!")

    elif message.content.startswith("!duck.slap"):
        name = message.content.split("!duck.slap ",1)[1] 
        await message.channel.send(f"{message.author} slapped {name} !!!!! That was brutal!!!")
   
    elif message.content == "!duck.fight":
        await message.channel.send(f"{message.author} started a foot fight in the cafeteria!!! Watch out for that taco....")

    elif message.content.startswith("!duck.challenge"):
        name = message.content.split("!duck.challenge ",1)[1] 
        await message.channel.send(f"{message.author} challenged {name} to a duel! \n Do you accept {name}? Or are you going to run away like a coward!!")
   
    elif message.content.startswith("!duck"):
        arg = message.content.split("!duck.",1)[1] 
        await message.channel.send(f"{message.author} {arg} is not an available option...")

client.run(token)
