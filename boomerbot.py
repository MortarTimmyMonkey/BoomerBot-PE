#BoomerBot PE
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import embed
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
    pingembed = discord.Embed(title = "Information", description = 'Pong! 555ms', colour = 475a85)
    
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
       kicksuccessembed = discord.Embed(title = "Information", description = "I kicked {}..format(user.name), colour = 475a85)
       await bot.kick(user)
    else:
       kickmissingembed = discord.Embed(title = "Oops!", description = "You need KICK MEMBERS permission to do that!", colour = 475a85)


#THIS MUST BE THIS WAY
bot.run(os.getenv('TOKEN'))
