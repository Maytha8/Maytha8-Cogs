from .restapi import RestApi

def setup(bot):
    bot.add_cog(RestApi(bot))
