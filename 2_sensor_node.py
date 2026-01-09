import time
import json
import random
import sys
import os
from azure.iot.device import IoTHubDeviceClient, exceptions

# 🛑 PASTE YOUR CONNECTION STRING HERE
CONNECTION_STRING = "HostName=xxxx;SharedAccessKey=xxxx"

def load_data(filename):
    if not os.path.exists(filename):
        return [40.0] * 600 # Fallback safe data
    with open(filename, 'r') as f:
        return [float(l.strip()) for l in f]

def run_mesh_network():
    print("\n⚡ LIFESIGNAL MESH NETWORK INITIALIZING...")
    
    # 1. Connect to Azure
    client = None
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        client.connect()
        print("✅ AZURE IOT HUB: CONNECTED")
    except:
        print("⚠️ OFFLINE MODE: Simulating Local Mesh...")

    # 2. Load Data for 3 Sensors
    # We simulate that Sensor A sees Human, B sees Human, C sees Human
    rubble_A = load_data('data_rubble.csv')
    human_A = load_data('data_human_A.csv')
    human_B = load_data('data_human_B.csv')
    human_C = load_data('data_human_C.csv')

    # Start in SCANNING mode
    streams = {
        "Sensor_Alpha": rubble_A,
        "Sensor_Beta":  rubble_A,
        "Sensor_Gamma": rubble_A
    }
    
    idx = 0
    packet_count = 0
    
    print("\n--- MESH ACTIVE ---")
    print(" 📡 Streaming data from 3 Nodes...")
    print(" ⏱️  Auto-Switch to TARGET FOUND in 15 seconds...\n")

    while True:
        try:
            # Loop data if end reached
            if idx >= 600: idx = 0

            # 1. READ FROM ALL 3 SENSORS
            for sensor_id, stream in streams.items():
                val = stream[idx] + random.uniform(-0.05, 0.05)
                
                msg = {
                    "device_id": sensor_id,
                    "csi_amp": val,
                    "battery": 98 - int(packet_count/100),
                    "timestamp": time.time()
                }

                # Send to Azure (Simulated Mesh)
                if client and packet_count % 5 == 0: # Reduce spam, send every 5th
                    try:
                        client.send_message(json.dumps(msg))
                    except: pass
            
            # Print status every 10 ticks
            if packet_count % 10 == 0:
                status = "SCANNING" if streams["Sensor_Alpha"] == rubble_A else "TARGET LOCKED"
                print(f"📡 MESH SYNC | Pkts: {packet_count} | Status: {status}")

            # --- THE MAGIC SWITCH (15 Seconds) ---
            if packet_count == 150 and streams["Sensor_Alpha"] == rubble_A:
                print("\n" + "█"*40)
                print("!!! ⚠️  TRIANGULATION SUCCESSFUL !!!")
                print("!!!     Switching all nodes to HUMAN     !!!")
                print("█"*40 + "\n")
                streams["Sensor_Alpha"] = human_A
                streams["Sensor_Beta"]  = human_B
                streams["Sensor_Gamma"] = human_C
                idx = 0

            time.sleep(0.1)
            idx += 1
            packet_count += 1
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run_mesh_network()