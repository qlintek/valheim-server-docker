import os
import a2s
from dotenv import load_dotenv

load_dotenv()

valheim_server_ip = os.getenv('VALHEIM_SERVER_IP')
valheim_query_port = int(os.getenv('VALHEIM_QUERY_PORT'))


def get_player_count(ip,port):
    try:
        info = a2s.info((ip, port))
        return info.player_count, info.max_players
    except Exception as e:
        logging.error(f"Error getting player count: {e}")
        return None , None
    

def get_server_status():
    try:
        info = a2s.info((VALHEIM_SERVER_IP, VALHEIM_QUERY_PORT))
        return {
            'name': info.server_name,
            'map': info.map,
            'players': info.player_count,
            'max_players': info.max_players,
            'password_protected': info.password_protected
        }
    except Exception as e:
        logging.error(f"Error getting server status: {e}")
        return None