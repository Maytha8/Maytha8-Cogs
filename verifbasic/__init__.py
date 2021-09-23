from redbot.core import commands

def setup(bot):
    bot.add_cog(VerifBasic(bot))

class VerifBasic(commands.Cog):
    """Basic verification"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        verifmsg = await self.bot.get_channel(887951332915429376).fetch_message(890383113681797150)
        await verifmsg.clear_reactions()
        await verifmsg.add_reaction('<:StoodVerif:890367558778245120>')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id == 890383113681797150 and not user.bot:
            await reaction.remove(user)
            await user.send("To verify, please complete this form: https://forms.gle/dPJnna9upwntBfMw7")
