import discord
from discord.ext import commands
from core.classes import Cog_extension
import json


with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class TempChannel(Cog_extension):
    temporary_channels = []

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState)    :
        possible_channel_name = jdata["Clone-Temp-Channel"] + f"{member.name}"
        if after.channel:
            if after.channel.name == jdata["Temp-Channel"]:
                temp_channel = await after.channel.clone(name = possible_channel_name)
                await member.move_to(temp_channel)
                await temp_channel.edit(user_limit = None)
                self.temporary_channels.append(temp_channel.id)

        if before.channel:
            if before.channel.id in self.temporary_channels:
                if len(before.channel.members) == 0:
                    await before.channel.delete()

async def setup(bot):
    await bot.add_cog(TempChannel(bot))