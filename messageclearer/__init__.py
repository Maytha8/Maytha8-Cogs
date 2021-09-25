from redbot.core import checks, commands

def setup(bot):
    bot.add_cog(MessageClearer(bot))

class MessageClearer(commands.Cog):
    """Clear messages and remove clutter."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.mod_or_permissions(manage_messages=True)
    @checks.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount_of_messages):
        """
        Clear <amount_of_messages> from the current channel.

        Will clear either the last <amount> messages, or, when 'all' is used, will clear the whole channel.
        """
        if ctx.channel.type != discord.ChannelType.text:
            return

        if amount_of_messages == 'all':
            await ctx.channel.purge(limit=None)
            botmsg = await ctx.send("Deleted all messages.")
            await botmsg.delete(delay=5)
        elif isinstance(amount_of_messages, int):
            await ctx.channel.purge(limit=amount_of_messages)
            botmsg = await ctx.send(f"Deleted {amount_of_messages} messages.")
            await botmsg.delete(delay=5)
        else:
            botmsg = await ctx.send("No number nor 'all' was specified.")
            await botmsg.delete(delay=5)
