from redbot.core import commands
import discord

def setup(bot):
    bot.add_cog(Invite(bot))

class Invite(commands.Cog):
    """Invite users to the server."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendinvite(self, ctx, user: discord.User):
        if self.bot.get_user(user.id):
            usr = self.bot.get_user(user.id)
            await usr.send("""**You are invited to join the Stood Server.**
            The Stood server is a study server dedicated to help you improve study and academical performance.
            You're not required to join, so you may decline the invite if you wish to do so.

            **Early Access**
            You are invited to become an Alpha Tester on the Stood Server.
            Alpha Testers will recieve exclusive recognision, and will be invited in special VIP events.

            Join now! discord.gg/gpFR7sFcjC

            For any issues or concerns, please DM <@!406762686261624832>.
            Regards, The Stood Team.""")
