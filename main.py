import math
import discord
from discord.ext import tasks
import random
import re
import os
from dotenv import load_dotenv
import sqlite3
import requests
import shutil
import urllib.request
import datetime
import subprocess
from func import download_image_class

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def search(name,guildid):
    con=sqlite3.connect("charaDB.db")
    result = con.execute("SELECT * FROM chara where name=? and guildID=?;",(name,guildid))
    for row in result:
        return row
    return 0


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("/test"):
        print(message.guild.id)
    if message.content.startswith("/ila "):
        msg=message.content.split(" ")
        print(msg[1])
        result=search(msg[1],message.guild.id)
        if result!=0:
          filepass=result[2]
          await message.channel.send(file=discord.File(filepass))
    if message.content.startswith("/ila　"):
        msg=message.content.split("　")
        result=search(msg[1],message.guild.id)
        if result!=0:
          filepass=result[2]
          await message.channel.send(file=discord.File(filepass))
    if message.content.startswith("/add "):
        msg=message.content.split(" ")
        date = datetime.datetime.now()
        con=sqlite3.connect("charaDB.db")
        filepass="img/"+date.strftime("%Y%m%d%H%M%S") + ".png"
        try:
            con.execute("INSERT INTO chara VALUES (?, ?, ?, ?)",(date.strftime("%Y%m%d%H%M%S"),msg[1],filepass,message.guild.id))
        except sqlite3.IntegrityError:
            con.rollback()
        finally:
            con.commit()
        download_image_class(message,filepass)
    if message.content.startswith("/add　"):
        msg=message.content.split("　")
        date = datetime.datetime.now()
        con=sqlite3.connect("charaDB.db")
        filepass="img/"+date.strftime("%Y%m%d%H%M%S") + ".png"
        try:
            con.execute("INSERT INTO chara VALUES (?, ?, ?, ?)",(date.strftime("%Y%m%d%H%M%S"),msg[1],filepass,message.guild.id))
        except sqlite3.IntegrityError:
            con.rollback()
        finally:
            con.commit()
        download_image_class(message,filepass)

load_dotenv()
client.run(os.getenv("TOKEN"))