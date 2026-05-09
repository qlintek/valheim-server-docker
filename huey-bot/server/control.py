def start_server():
    try:
        result = subprocess.run(['docker', 'start', VALHEIM_CONTAINER_NAME], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Started server container: {VALHEIM_CONTAINER_NAME}")
            return True
        else:
            logging.error(f"Failed to start server container: {result.stderr}")
            return False
    except Exception as e:
        logging.error(f"Error starting server container: {e}")
        return False
    
def stop_server():
    try:
        result = subprocess.run(['docker', 'stop', VALHEIM_CONTAINER_NAME], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Stopped server container: {VALHEIM_CONTAINER_NAME}")
            return True
        else:
            logging.error(f"Failed to stop server container: {result.stderr}")
            return False
    except Exception as e:
        logging.error(f"Error stopping server container: {e}")
        return False
    
def restart_server():
    try:
        result = subprocess.run(['docker', 'restart', VALHEIM_CONTAINER_NAME], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Restarted server container: {VALHEIM_CONTAINER_NAME}")
            return True
        else:
            logging.error(f"Failed to restart server container: {result.stderr}")
            return False
    except Exception as e:
        logging.error(f"Error restarting server container: {e}")
        return False