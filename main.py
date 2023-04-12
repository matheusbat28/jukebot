from decouple import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    
@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("você não está em um canal de voz!")
        return
    else:
        channel = ctx.author.voice.channel
    await channel.connect()
    
bot.run(config('TOKEN'))


@bot.command()
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send("não estou em um canal de voz!")
        return
    else:
        await ctx.guild.voice_client.disconnect()