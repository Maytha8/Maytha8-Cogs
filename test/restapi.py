from redbot.core import commands

class Test(commands.Cog):
    """REST API endpoint."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testcom(self, ctx):
        """Test command for REST API."""
        await ctx.send("REST API up and running!")
