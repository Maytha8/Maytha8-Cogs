from redbot.core import commands

class RestApi(commands.Cog):
    """REST API endpoint."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def restapi(self, ctx):
        """Test command for REST API."""
        await ctx.send("REST API up and running!")
        await ctx.send(type(self).__module__)

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     await message.add_reaction(":happy:")
