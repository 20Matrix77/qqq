import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1208155463795867648)
    if channel:
        await channel.send("```[Linux]: B0t c0nnected```")
    else:
        print("Channel not found")

bot.run('MTIwODEzMjEyODU2NzU5MTAwMw.GBOBrh.6rc_ZCuZdkcrFXrbKrxX2aST-WYcAbtbjsD294')
