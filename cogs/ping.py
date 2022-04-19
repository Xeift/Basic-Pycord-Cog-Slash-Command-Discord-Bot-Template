import discord
from discord.commands import slash_command
from discord.ext import commands
from core.cog_core import cogcore

class ping(cogcore):
    @slash_command(guild_ids=[936236815545954384],name='ping',description='return bot latency')
    async def ping(
        self,
        ctx: discord.ApplicationContext
    ):
        await ctx.respond(f"pong! ({self.bot.latency*1000:.2f} ms)")
def setup(bot):# add cog
    bot.add_cog(ping(bot))
