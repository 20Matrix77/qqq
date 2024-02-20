import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1208155463795867648)
    await channel.send(f"```Linux-> B0t c0nnected```")

bot.run('MTIwODEzMjEyODU2NzU5MTAwMw.G7SIu8.nHYc9en0jM_RijBrAO6Ecv-ivvkh9w7_1X2cNs')
