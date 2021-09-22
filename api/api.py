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
