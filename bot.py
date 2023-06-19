import discord
from discord.ext import commands, tasks
import json
import os
import asyncio

with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = jdata["Prefix"], intents = intents)

#bot.remove_command("help")

@bot.event
async def on_ready():
    await load_cogs()
    await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = jdata["Bot-Status"]))
    task_loop.start()
    print(">> Bot Is Online <<")

@tasks.loop(seconds = 3)
async def task_loop():
    #
    #
    #
    #
    #
    #
    pass

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await bot.start(jdata["TOKEN"])

asyncio.run(main())