import discord

bot = discord.Bot(intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

extensions = [# load cogs
  'cogs.ping'
]

if __name__ == '__main__':# import cogs from cogs folder
	for extension in extensions:
		bot.load_extension(extension) 
        
bot.run("YOUR_BOT_TOKEN_FROM_DEV_PORTAL")# bot token
