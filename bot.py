import discord

TOKEN = 'TOKEN DU BOT'
client = discord.Client()



@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name='LE NOM'))
	print("bot démarré avec le nom de {0.user}".format(client))


@client.event
async def on_message(message):
	username = str(message.author).split('=')[0]
	message_content = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {message_content} ({channel})')

	if message.author == client.user:
		return

	end_mess = message_content.endswith
	if end_mess("quoi") or end_mess("quoi?") or end_mess("quoi ?") or end_mess("Quoi") or end_mess("Quoi?") or end_mess("Quoi ?"):
		await message.channel.send(f'feur')
		return




client.run(TOKEN)
