# Use carefully!

import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print("Ready to go! :3")

@bot.command(pass_context=True)
async def deleteall(ctx, channel):
	for channel in ctx.message.author.server.channels:
		await bot.delete_channel(channel)
		
		
@bot.command(pass_context=True)
async def banall(ctx, member):
	for member in ctx.message.author.server.members:
		await bot.ban(member)
		
bot.run("YOUR TOKEN GOES HERE")
