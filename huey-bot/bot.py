from asyncio import tasks

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import subprocess
import a2s
import datetime
from .config import DISCORD_TOKEN, VALHEIM_SERVER_IP, VALHEIM_QUERY_PORT, VALHEIM_CONTAINER_NAME
from server.control import start_server, stop_server, restart_server
from server.query import get_server_status, get_player_count    

#My Code I am importing
from .control import start_server, stop_server, restart_server
from .query import get_server_status, get_player_count


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


bot.command(name = "players")
async def players(ctx):
    players, max_players = get_player_count(VALHEIM_SERVER_IP, VALHEIM_QUERY_PORT)
    if players is None:
        await ctx.send("Unable to retrieve player count.")
        return
    await ctx.send(f"Current players: {players}/{max_players}")
    

    

    