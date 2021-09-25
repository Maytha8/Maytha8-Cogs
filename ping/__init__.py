from redbot.core import commands

def setup(bot):
    bot.add_cog(Ping(bot))

class Ping(commands.Cog):
    """Ping users on announcements."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if "[PING]" in msg.content:
            if msg.channel.id == 888355679469989918:
                await self.bot.get_channel(888355679469989918).send("> @everyone <:this:891123206457544714>")
            elif msg.channel.id == 891118316758925355:
                await self.bot.get_channel(891118316758925355).send("> <@&891122442431524864> <:this:891123206457544714>")
