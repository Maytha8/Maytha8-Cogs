from redbot.core import commands

def setup(bot):
    bot.add_cog(Polls(bot))

class Polls(commands.Cog):
    """Create polls."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id == 890539259646345266:
            if "[POLL]" in msg.content:
                await msg.add_reaction('✅')
                await msg.add_reaction('❌')
            elif "[RATE]" in msg.content:
                await msg.add_reaction('1')
                await msg.add_reaction('2')
                await msg.add_reaction('3')
                await msg.add_reaction('4')
                await msg.add_reaction('5')
