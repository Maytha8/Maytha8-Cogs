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

    @commands.command()
    async def verifinit(self, ctx):
        verifmsg = self.bot.get_channel(887951332915429376).fetch_message(890366650703028305)
        await verifmsg.clear_reactions()
        await verifmsg.add_reaction('StoodVerif')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.id != self.bot.user.id:
            await msg.reply("Hi!")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id == 890366650703028305:
            await reaction.remove(user)
            await user.send("To verify, please complete this form: https://forms.gle/dPJnna9upwntBfMw7")

# 887950654113464350/887951332915429376/890366650703028305
