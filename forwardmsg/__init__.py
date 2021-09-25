# https://discord.com/api/webhooks/890879948330512384/RnihXQZiitzpFVOYxeZ0wMjctdPv7Q51Vs6AuvYflxmVVZYZSLHlbO8Yw1Yi-xap6lPv
from redbot.core import commands
import asyncio
import discord

def setup(bot):
    bot.add_cog(ForwardMsg(bot))

class ForwardMsg(commands.Cog):
    """Forward messages as bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id == 890879683015626772 and msg.author.name == "Stood Messages":
            await self.bot.get_channel(890879683015626772).send("Type in which channel to forward to, or reply with 'cancel'.")

            def check(reply):
                return not reply.author.bot and reply.author.name != "Stood Messages" and len(reply.channel_mentions) != 0 and reply.channel.id == 890879683015626772 and reply.channel_mentions[0].type == discord.ChannelType.text

            try:
                reply = await self.bot.wait_for('message', timeout=20, check=check)
            except asyncio.TimeoutError:
                await self.bot.get_channel(890879683015626772).send("No response. Cancelling.")

            if (reply.content.lower() == 'cancel'):
                await self.bot.get_channel(890879683015626772).send("Cancelling.")
            else:
                await reply.channel_mentions[0].send(msg.content, embed=msg.embeds[0])
