from redbot.core import commands

class api(commands.Cog):
    """My custom API cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def apistatus(self, ctx):
        """Test API status!"""
        # Your code will go here
        await ctx.send("API is up and running!")
        await ctx.send(type(ctx).__module__)

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.author.id != self.bot.user.id:
    #         await msg.reply("Hi!")

# https://discord.com/channels/887950654113464350/887951332915429376/890383113681797150
