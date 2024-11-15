import discord
from discord.ext import commands
import json
import os

# Load configuration
with open("config.json") as config_file:
    config = json.load(config_file)

# Initialize bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Load commands from the 'commands' folder
for file in os.listdir("src/commands"):
    if file.endswith(".py") and file != "__init__.py":
        bot.load_extension(f"commands.{file[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected!")
    print(f"Prefix: {config['prefix']}")

bot.run(config["token"])
