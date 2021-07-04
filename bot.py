# Base Imports
from discord.ext import commands
from dotenv import load_dotenv
import builtins
import discord
import os

# Basic Variables
dev_mode = True
builtins.dev_mode = dev_mode

version = "1.0"
default_prefix = "="

# Connect to ENV file
load_dotenv(".env")

# Declare bot Intents
intents = discord.Intents.all()

# Create the bot
bot = commands.Bot(command_prefix=commands.when_mentioned_or(default_prefix), case_insensitive=True, intents=intents)
builtins.bot = bot


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to discord.")
    print("Loading cogs...")
    import commands
    bot.add_cog(commands.Commands())
    print("Cogs Loaded.")


# Start the bot
bot.run(os.getenv("TOKEN"))
