import discord
import os
import asyncio
import random
from discord.ext import commands

#---------------------------------
token = "your discord bot token"
#---------------------------------

bot = commands.Bot(command_prefix='!duck.')
client = discord.Client()

bad_words = ["fucker", "stupid", "fucking", "asshole", "shit", "fuck", "dumb", "ass", "nigger", "dick", "but"]

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@client.event
async def on_ready():
    print("Started bot as {0.user}".format(client))

    for server in client.servers:
        for channel in server.channels:
            if channel.type == 'Text':
                channel = client.get_channel(channel)
                await channel.send("Hello! I am B0B. I am a bot that hates violence and swearing. \n Use '!duck.help' to list all my commands. \n You can also use '!duck.info' so I can introduce myself.")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    elif any (word in message for word in bad_words):
        await message.channel.send("You motherfucker! Stop fucking around with those bad words asshole!!!!!")

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
        await client.send_message("Welcome to this server " + member)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
        await client.send_message(member + " left the server. Fuck you!!!!")

@bot.command()
async def info(ctx):
    await ctx.send("Hello! I am B0B. I am a bot that hates violence and swearing. \n Use '!duck.help' to list all my commands.")

@bot.command()
async def help(ctx):
    await ctx.send("List of all B0B commands: \n !duck.duck = If you want to duck someone. \n !duck.slap = Slap someone.")

@bot.command()
async def duck(ctx, name):
    await ctx.send("Fuck " + name + "!!!!!")

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

client.run(token)
