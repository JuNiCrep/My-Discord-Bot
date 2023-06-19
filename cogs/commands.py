import discord
from discord.ext import commands
from core.classes import Cog_extension
import json


with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class Commands(Cog_extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency * 1000)}ms!")

    @commands.command()
    @commands.has_role(jdata["Admin-Role"])
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit = num + 1)

async def setup(bot):
    await bot.add_cog(Commands(bot))