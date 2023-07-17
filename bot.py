import discord
from discord.ext import commands
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv
import os
import json

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DEV_TELEGRAM_GROUP_ID = os.getenv('DEV_TELEGRAM_GROUP_ID')
DISCORD_TEST_CHANNEL_ID = os.getenv('DISCORD_TEST_CHANNEL_ID')
DISCORD_CHANNEL_IDS = os.getenv('DISCORD_CHANNEL_IDS')

if DISCORD_CHANNEL_IDS:
    DISCORD_CHANNEL_IDS = json.loads(DISCORD_CHANNEL_IDS) 

if DISCORD_TEST_CHANNEL_ID:
    DISCORD_TEST_CHANNEL_ID = int(DISCORD_TEST_CHANNEL_ID)

IMAP_SERVER = os.getenv('IMAP_SERVER')
EMAILS_JSON = os.getenv('EMAILS')
EMAILS = json.loads(EMAILS_JSON)

intents = discord.Intents.default()
intents.message_content = True

discord_bot = commands.Bot(command_prefix='!', intents=intents)
telegram_bot = Bot(TELEGRAM_TOKEN)

@discord_bot.event
async def on_ready():
    print(f'Bot de Discord listo: {discord_bot.user.name}')

@discord_bot.event
async def on_message(message):
    
    if (message.channel.id == DISCORD_TEST_CHANNEL_ID or message.channel.id in DISCORD_CHANNEL_IDS) and message.author != discord_bot.user:

        guild = message.guild
        content = message.content
        author = message.author.global_name
        text = f"**DISCORD: {guild}** \n **{author}:** " + content
        await telegram_bot.send_message(DEV_TELEGRAM_GROUP_ID, text=text, parse_mode=ParseMode.MARKDOWN_V2)
    
    await discord_bot.process_commands(message)

discord_bot.run(DISCORD_TOKEN)

