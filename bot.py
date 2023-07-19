import discord
from discord.ext import commands, tasks
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv
import os
import json
import mail_tools

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

@tasks.loop(minutes=10)
async def email_routine():
    print("Checking Email Routine")
    for email, password in EMAILS.items():
        print(f"Checking {email}")
        new_mail = mail_tools.check_emails(email, password, IMAP_SERVER)
        for mail in new_mail:
            content, name, addr, date, subject = mail
            text = f"<b>EMAIL - {email}</b> \n <b>{date}</b> \n <b>{addr} : {name}</b> \n\n {content}"
            await telegram_bot.send_message(DEV_TELEGRAM_GROUP_ID, text=text, parse_mode=ParseMode.HTML)

@discord_bot.event
async def on_ready():
    email_routine.start()
    print(f'Bot de Discord listo: {discord_bot.user.name}')

@discord_bot.event
async def on_message(message):
    
    if (message.channel.id == DISCORD_TEST_CHANNEL_ID or message.channel.id in DISCORD_CHANNEL_IDS) and message.author != discord_bot.user:

        guild = message.guild
        content = message.content
        author = message.author.global_name
        text = f"<b>DISCORD - {guild}</b> \n <b>{author}:</b> " + content
        await telegram_bot.send_message(DEV_TELEGRAM_GROUP_ID, text=text, parse_mode=ParseMode.HTML)
    
    await discord_bot.process_commands(message)

discord_bot.run(DISCORD_TOKEN)

