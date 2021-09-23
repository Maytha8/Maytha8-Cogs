import asyncio
import discord
import datetime
from redbot.core import commands

def setup(bot):
    bot.add_cog(VerifPlus(bot))

class VerifPlus(commands.Cog):
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
            embed = discord.Embed(
                title="Entry Verification",
                colour=discord.Colour(3173631),
                description="Verify your identity to join the Stood Server."
            )

            def check(reaction, usr):
                return (usr == user and msg == reaction.message) and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')

            await user.send(embed=embed)
            msg = await user.send("Would you like to start verification?")
            await msg.add_reaction('✅')
            await msg.add_reaction('❌')

            try:
                reaction, usr = await self.bot.wait_for("reaction_add", check=check, timeout=30)
            except asyncio.TimeoutError:
                user.send("You took too long to respond. Cancelling.")
                return

            if str(reaction.emoji) == '❌':
                user.send("You responded with ❌. Cancelling.")
                return
