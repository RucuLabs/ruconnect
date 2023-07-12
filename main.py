import discord
from discord.ext import commands
from telegram import Bot

# Configura los tokens de los bots de Discord y Telegram
DISCORD_TOKEN = 'TOKEN'
TELEGRAM_TOKEN = 'TOKEN'

# Configura el ID del grupo de Telegram al que se enviarán los mensajes
TELEGRAM_GROUP_ID = '-ID'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents )
telegram_bot = Bot(TELEGRAM_TOKEN)

@bot.event
async def on_ready():
    print(f'Bot de Discord listo: {bot.user.name}')

@bot.event
async def on_message(message):
    print(message.channel.id)
    if message.channel.id == 123 and message.author != bot.user:
        content = message.content
        text = f"{message.author.global_name}: " + content
        await telegram_bot.send_message(TELEGRAM_GROUP_ID, text=text)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
