import json
import time
import websockets  # Use the websockets library for WebSocket communication
import asyncio
import data_collection

# Define the server URL where you will send the data
server_url = "ws://127.0.0.1:8765"  # Update the URL to use WebSocket

def collect_system_data():
    hostname = data_collection.get_hostname()
    ip_address = data_collection.get_ip_address()
    uptime = data_collection.get_uptime()
    mac_address = data_collection.get_mac_address()

    data = {
        "hostname": hostname,
        "ip_address": ip_address,
        "uptime": uptime,
        "mac_address": mac_address,
        # Add more data fields as needed
    }
    return data


async def send_data_to_server(data):
    async with websockets.connect(server_url) as websocket:
        await websocket.send(json.dumps(data))
        print("Data sent successfully.")

if __name__ == "__main__":
    while True:
        data = collect_system_data()
        asyncio.get_event_loop().run_until_complete(send_data_to_server(data))

        # Adjust the interval (in seconds) based on your needs
        time.sleep(60)  # Send data every 1 minute
