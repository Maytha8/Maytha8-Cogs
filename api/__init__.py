from .api import api


def setup(bot):
    bot.add_cog(api(bot))
