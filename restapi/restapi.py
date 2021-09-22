from redbot.core import commands

class MyCog(commands.Cog):
    """REST API endpoint."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def apicom(self, ctx):
        """Test command for REST API."""
        await ctx.send("REST API up and running!")
        #await ctx.send(type(self).__module__)
