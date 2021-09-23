from redbot.core import commands
import discord

def setup(bot):
    bot.add_cog(Invite(bot))

class Invite(commands.Cog):
    """Invite users to the server."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendinvite(self, ctx, usr: discord.User):
        if self.bot.get_user(user.id):
            user = self.bot.get_user(user.id)
            user.send("**We invite you to the Stood server.**\nThe Stood server is a study server dedicated to help you improve study and academical performance.\n\nJoin now! discord.gg/gpFR7sFcjC\n\nYou're not required to join, so you may decline the invite if you wish to do so.\n\nFor any issues or concerns, please DM <@!406762686261624832>.\n\nRegards, The Stood Team.")
