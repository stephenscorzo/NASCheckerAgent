import asyncio
import websockets
import json


async def process_data(websocket, path):
    async for message in websocket:
        try:
            data = json.loads(message)

            # Process the data as needed
            insert_data_into_database(data)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
