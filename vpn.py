import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(INSERT_YOUR_CHANNEL_ID)
    await channel.send(f"```Linux-> Б0т п0дключен```")

bot.run('MTIwODEzMjEyODU2NzU5MTAwMw.G7SIu8.nHYc9en0jM_RijBrAO6Ecv-ivvkh9w7_1X2cNs')
