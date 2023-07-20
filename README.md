# RuConnect
Discord and Telegram bot designed to streamline management and facilitate effective communication within a small development team.

## Why?
RuConnects is a platform designed to facilitate connections between your small development team and the people you collaborate with, even when they use different communication channels such as Discord or Email.

## What?
You can connect:
- Any ammount of emails you want
- Any ammount of discord channels you want

With:
- One telegram group

## Dependencies
- Python 3.11.3
- Discord.py
- python-telegram-bot

## Configuration
Here is an example for your `.env` file.

```
DISCORD_TOKEN = DISC_TOKEN
TELEGRAM_TOKEN = TEL_TOKEN

DEV_TELEGRAM_GROUP_ID = GROUP_ID

DISCORD_TEST_CHANNEL_ID = TEST_CHANNEL_ID
DISCORD_CHANNEL_IDS = "[CHANNEL_ID, ANOTHER_CHANNEL_ID, ...]"

IMAP_SERVER = IMAP_SERVER
EMAILS = '{"user1@domain": "pass1", "user2@domain": "pass2", ...}'
```

## TODOs
- Add setup instructions
- Explain usage
- Explain how to get some of the env vars
