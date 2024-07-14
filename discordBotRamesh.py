import discord
import os
from selenium import webdriver
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from tkinter import Tk

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


client = discord.Client()
#token = os.getenv['token']

feelings = [
"Depressed, just like you lmao",
"sed. very sed.",
"horny.",
"*In a calm tone* I wanna die.",
"Felling like a GOD DAMN GAMER!"
"I feel epic."
]
gaali = ['smol brain',"you got a small peepee", "ur mom gae, haha.","i'm out of ideas"]

greetings = ["Hello ", "Hi ", "Greetings ", "Good Morning "]

songs = ["lonely","ocean eyes","despacito"]

def Link():
	driver = webdriver.Chrome(executable_path=PATH, chrome_options=option)
	driver.get("https://skribbl.io/")
	privateButton = driver.find_element_by_id("buttonLoginCreatePrivate")
	privateButton.click()
	time.sleep(5)
	select = Select(driver.find_element_by_id('lobbySetRounds'))
	select.select_by_visible_text('6')
	linkCopy = driver.find_element_by_id("inviteCopyButton")
	linkCopy.click()
	link = Tk().clipboard_get()
	
	return link



@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	print(message.content)
	if message.author == client.user:
		return

	elif message.content.startswith(".") or message.content.lower().startswith("ram") or message.content.lower().startswith("ramesh"):
		if "hello" in message.content or "hi" in message.content:
			await message.channel.send(random.choice(greetings) + message.author.name + "! What's up?")
		if "introduce" in message.content:
			await message.channel.send("Hallo mate! I am Ramesh, your epic 69 LMAO bot!")
		if "epic" in message.content:
			await message.channel.send("hehe boi.")
		if "gaali" in message.content or "curse" in message.content:
			await message.channel.send(random.choice(gaali))
		if "talk to suresh" in message.content:
			await message.channel.send("suresh biro, I am Ramesh. How are you?")
		if "how are you" in message.content:
			await message.channel.send(random.choice(feelings))
		
		if "I am Suresh" in message.content:		
				await message.channel.send("suresh biro Hallo! Nice to meet you!")
		
		if "Nice to meet you!" in message.content:
			await message.channel.send("Nice to meet you too beb <3 :*")
		
		if "❤️" in message.content or "<3" in message.content:
			await message.channel.send("Ily 💖 UwU")
		
		if "say" in message.content:
			new = message.content.replace("ramesh","")
			new = message.content.replace(".","")
			new = new.replace("say","")
			await message.channel.send(new)

		if "feeling sad" in message.content:
			await message.channel.send("Alexa, play "+random.choice(songs)+".")
		
		if "skribbl" in message.content:
			await message.channel.send("Control yo' pp for a fkn sec!")
			await message.channel.send(Link())
		if "tarang" in message.content and "birthday" in message.content:
			await message.channel.send("Happy Birthday taaraanngg, happy birthday tarangg, happy birthday tarang, happy birthday taraaaannnnngggg!!!!🥳🎈🥳🎈🎈🎈🎊🎊🎂🎂 WHOOOOOOOOOOOOOOOOOOOO!!!!!")




client.run("ODQwODkzODY2OTQwNjk0NTI5.YJe1cA.0XvPDfE3I1w2YhYADVZaB_8YL_8")
