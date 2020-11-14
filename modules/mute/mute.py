import json
import random
from discord.ext import commands
import asyncio
import traceback
import discord


class mute(commands.Cog, name = "mute"):

    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("mute Module Loaded")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self,ctx, member:discord.Member,time:str,*,reason = 'No reason provided'):
        try:
            while True:
                try:
                    if member == ctx.message.author:
                        embed = discord.Embed(title = 'No you may not mute yourself.')
                        await ctx.send(embed = embed)
                        break
                    else:
                        indicator = time[-1]
                        if indicator == "m" or indicator == "s" or indicator == 'h' or indicator == 'd':
                            pass
                        else:
                            await ctx.send('Incorrect Time Format.')
                            break
                        muted_give = discord.utils.get(ctx.guild.roles, name = 'Muted')
                        await member.add_roles(muted_give)
                        embed = discord.Embed(title = str(member) + ' was successfully muted by: ' + str(ctx.author) + ' for ' + str(time))
                        await ctx.send(embed = embed)
                        time = time[:-1]
                        if indicator == 'm':
                            await asyncio.sleep(int(time) * 60)
                        elif indicator == 'h':
                            await asyncio.sleep(int(time) * 3600)
                        elif indicator == 's':
                            await asyncio.sleep(int(time))
                        elif indicator == 'd':
                            await asyncio.sleep(int(time) * 86400)
                        await member.remove_roles(muted_give)
                        break
                except AttributeError:
                    muted = await ctx.guild.create_role(name = "Muted")
                    await ctx.message.channel.set_permissions(ctx.guild.get_role(muted.id), send_messages = False)
        except Exception:
            traceback.print_exc()

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unmute(self,ctx,member: discord.Member,*,reason = "No reason provided"):
        muted_remove = discord.utils.get(ctx.guild.roles, name = 'Muted')
        await member.remove_roles(muted_remove)
        embed = discord.Embed(title = str(member) + ' was successfully unmuted by: ' + str(ctx.author))
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(mute(bot))