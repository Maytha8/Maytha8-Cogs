from redbot.core import commands, tasks
from aiohttp import web
import aiohttp
import os

app = web.Application()
routes = web.RouteTableDef()

class api(commands.Cog):
    """My custom API cog"""

    def __init__(self, bot):
        self.bot = bot
        self.web_server.start()

        @routes.get('/')
        async def welcome(request):
            return web.Response(text="Hello, world!")

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host='0.0.0.0', port=self.webserver_port)
        await site.start()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def apistatus(self, ctx):
        """Test API status!"""
        # Your code will go here
        await ctx.send("API is up and running!")
        await ctx.send(type(ctx).__module__)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.id != self.bot.user.id:
            await msg.reply("Hi!")
