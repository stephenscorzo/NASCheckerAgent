import asyncio
import websockets
from databasefunctions import create_database_connection, insert_data_into_database
from websocketserver import process_data


# Define your server configuration
server_host = '0.0.0.0'  # Your server's IP address or '0.0.0.0' to listen on all interfaces
server_port = 8765  # Choose the appropriate port



if __name__ == "__main__":
    start_server = websockets.serve(process_data, server_host, server_port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
