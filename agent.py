import requests
import json
import time
import psutil  # You may need to install the psutil library using pip

# Define the server URL where you will send the data
server_url = "https://your-server-url.com/api/endpoint"

def collect_system_data():
    # Implement data collection functions
    hostname = "ClientHostname"
    ip_address = "192.168.1.100"
    uptime = int(time.time())  # Sample uptime in seconds
    # Add more data collection logic here

    data = {
        "hostname": hostname,
        "ip_address": ip_address,
        "uptime": uptime,
        # Add more data fields here
    }

    return data

def send_data_to_server(data):
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(server_url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {str(e)}")

if __name__ == "__main__":
    while True:
        data = collect_system_data()
        send_data_to_server(data)

        # Adjust the interval (in seconds) based on your needs
        time.sleep(60)  # Send data every 1 minute