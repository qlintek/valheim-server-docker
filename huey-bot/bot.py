from asyncio import tasks

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import subprocess
import a2s
import datetime

load_dotenv()
#Values that can be set in .env file and will need to be called to perform certain tasks. These include the bot token, the IP and query port of the Valheim server, and the name of the Valheim server container.
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
VALHEIM_SERVER_IP = os.getenv('VALHEIM_SERVER_IP')
VALHEIM_QUERY_PORT = int(os.getenv('VALHEIM_QUERY_PORT'))
VALHEIM_CONTAINER_NAME = os.getenv('VALHEIM_CONTAINER_NAME')
#EMPTY_THRESHOLD = int(os.getenv('EMPTY_THRESHOLD'))
#CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL'))

os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

