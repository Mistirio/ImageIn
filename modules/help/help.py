from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self , client):
        self.client = client
    @commands.command()
    async def help(self , ctx):
        embed = discord.Embed(title='ImageIn Help',
                              description='An Epic image manipulation bot')
        embed.add_field(name="Image Commands",
                        value=f"`trash`, `burn`, `slap`, `wanted`, `rip`, `gun`,`youtried`,`eat`,`really`",
                        inline=False)
        """
        embed.add_field(name="Moderation Commands",
                        value=f"`{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`",
                        inline=False)
        embed.add_field(name="General Fun Commands",
                        value=f"`{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`",
                        inline=False)
        embed.add_field(name="Welcome Commands",
                        value=f"`{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`",
                        inline=False)
        embed.add_field(name="Setup Commands",
                        value=f"`{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`, `{prefix}placeholder`",
                        inline=False)
        """
        embed.add_field(name="Support Server", value=f"[`Click Here!`](https://discord.gg/hJ93yrh)", inline=True)
        embed.add_field(name="Website", value=f"[`Click Here!`](https://imagein-bot.gq/)", inline=True)
        embed.add_field(name="Top.gg", value=f"[`Click Here!`]()", inline=True)


def setup(client):
    client.add_cog(Help(client))