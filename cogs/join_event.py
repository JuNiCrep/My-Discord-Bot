import discord
from discord.ext import commands
from core.classes import Cog_extension
import datetime
import json


with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        Time = datetime.datetime.now()
        channel = self.bot.get_channel(int(jdata["Welcome-Channel"]))
        embed = discord.Embed(description = f"**{member.mention}, Welcome to the server!**", timestamp = Time)
        await channel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Event(bot))