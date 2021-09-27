from redbot.core import commands, checks
import discord
from requests import get

# from requests import get ip = get('https://api.ipify.org').text print(f'My public IP address is: {ip}')

def setup(bot):
    bot.add_cog(PublicIP(bot))

class PublicIP(commands.Cog):
    """Get public IP of bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def ip(self, ctx):
        ip = get('https://api.ipify.org').text
        if ctx.channel.type == discord.ChannelType.private:
            ctx.author.send(f"IP address is: {ip}")
        else:
            ctx.send("As the IP should stay private, it has been sent in your DM.")
            ctx.author.send(f"IP address is: {ip}")
