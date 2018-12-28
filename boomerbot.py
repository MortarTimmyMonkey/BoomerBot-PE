#BoomerBot PE

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='b!')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="b!help | 2 Servers"))

@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(
           title = "Information",
           description = "Pong! 555ms"
           colour = discord.Colour.blue()
           print ("user has pinged")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
       embed = discord.Embed(
           title = "Information",
           description="I kicked {}.".format(user.name),
           colour = discord.Colour.blue()
       await bot.kick(user)
    else:
       embed = discord.Embed(
           title = "Oops!",
           description ="You need KICK MEMBERS permission to do that`
           KICK MEMBERS permission to do that!"
           colour = discord.Colour.red()


#THIS MUST BE THIS WAY
bot.run(os.getenv('TOKEN'))
