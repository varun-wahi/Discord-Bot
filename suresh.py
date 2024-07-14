import discord
import os
import json
import requests
import random



client = discord.Client()

#token = os.getenv['token']
roast_words = [
"हे भगवान्! आप कितने मंदबुद्धि है.",
"I looked through your DM's and found out that you have a very small peepee",

]

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	print("recieved")
	if message.author == client.user:
		return

	elif message.content.startswith("suresh"):
		if "talk to ramesh" in message.content:
			await message.channel.send("ramesh biro, I am Suresh. Nice to meet you!")
		if "I am Ramesh" in message.content:
			await message.channel.send("ramesh bhai Hello! Nice to meet you!")
		if "Nice to meet you" in message.content:
			await message.channel.send("ramesh <3 :*")

client.run("ODQxMDMxNTg4MjUwNTE3NTg2.YJg1tA.LSYfSVExz4Uzs-dgIrr3q9h195M")
