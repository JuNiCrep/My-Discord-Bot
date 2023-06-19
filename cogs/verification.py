import discord
from discord.ext import commands
from core.classes import Cog_extension
import json

with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)
    
class Verified(Cog_extension):
    @commands.command()
    @commands.has_role(jdata["Admin-Role"])
    async def verification(self, ctx):
        embed = discord.Embed(title = "**Verification**")
        embed.add_field(name = "**Click ✅ To Verify!**", value = "", inline = True)
        await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == int(jdata["Verification-Message-ID"]):
            guild = self.bot.get_guild(payload.guild_id)
            role = guild.get_role(int(jdata["Verification-Role-ID"]))
            await payload.member.add_roles(role)

async def setup(bot):
    await bot.add_cog(Verified(bot))