
📡 LifeSignal: AI-Powered Disaster Response System
"Seeing the Unseen." > LifeSignal is a Digital Twin prototype that uses Wi-Fi sensing and Microsoft Azure to detect the respiratory signatures of earthquake victims trapped under rubble.

📖 Table of Contents
The Problem
The Solution
Key Features
System Architecture
Tech Stack
Installation & Setup
Usage Guide
Demo Scenarios
Team


🚨 The Problem:
In the aftermath of building collapses, the "Golden Hour" determines survival. Traditional rescue methods (cameras, dogs, acoustic sensors) fail when victims are:
Invisible (buried under concrete).
Silent (unconscious or unable to shout).
Inaccessible (deep within the void).
Rescuers are effectively blind, and thousands of "silent" victims are left behind.

💡 The Solution:
LifeSignal creates a "Droppable Mesh" of IoT sensors that repurpose standard Wi-Fi signals to detect micro-movements. By analyzing Channel State Information (CSI), our AI filters out rubble noise and locks onto the specific 0.25 Hz frequency of human respiration.

✨ Key Features:
📡 Multi-Sensor Mesh Network: Simulates 3 distinct IoT nodes (Alpha, Beta, Gamma) streaming real-time telemetry to Azure IoT Hub.
🧠 Azure AI Anomaly Detector: Logic to distinguish between random rubble shifts and rhythmic breathing patterns.
📍 Geospatial Triangulation: Integrated Azure Maps API to pinpoint the exact sector of the victim.
🗣️ Inclusive Design: Integrated Azure AI Translator allows international rescue teams to view critical alerts in their native language (Hindi, Spanish, French, etc.).
📊 FFT Spectral Analysis: Real-time Fast Fourier Transform graph proving the signal is biological (showing the 0.25Hz peak).

System Architecture:
graph TD
    A[Physics Data Engine] -->|Generates Synthetic CSI| B(IoT Sensor Mesh)
    B -->|Stream via MQTT| C{Azure IoT Hub}
    C -->|JSON Telemetry| D[Python Logic Layer]
    D -->|Signal Processing| E[Azure AI Anomaly Detector]
    D -->|Geolocation| F[Azure Maps API]
    E -->|Status: CRITICAL| G[Streamlit Commander Dashboard]
    F -->|Coords| G
    H[Azure AI Translator] -->|Localize Alerts| G

🛠 Tech Stack
Core Language: Python 3.10+
Cloud Platform: Microsoft Azure
Azure IoT Hub (Data Ingestion)
Azure Maps (Location Services)
Azure AI Translator (Accessibility)
Data Science: NumPy, Pandas, SciPy (FFT Analysis)
Visualization: Streamlit, Plotly Interactive Graphs

Installation and Setup:
1.Clone the Repository
  git clone https://github.com/YourUsername/LifeSignal.git
  cd LifeSignal
2.Install Dependencies
  pip install -r requirements.txt
(Ensure your requirements.txt includes: azure-iot-device, streamlit, pandas, numpy, plotly, requests)
3 . Configure Azure Keys
Open 3_dashboard.py and 2_sensor_node.py to update your keys:
IoT Hub Connection String: In 2_sensor_node.py
Azure Maps Key: In 3_dashboard.py
Azure Translator Key: In 3_dashboard.py
🚀 Usage Guide
Step 1: Generate Physics Data
    Creates synthetic physiological signal data for the demo.
    python 1_generate_data.py
Step 2: Initialize Sensor Mesh (The Backend)
    Starts the 3 simulated ESP32 nodes connecting to Azure.
    python 2_sensor_node.py
Step 3: Launch Commander Dashboard (The Frontend)
    Opens the web interface in your browser.
    streamlit run 3_dashboard.py


🎬 Demo Scenarios
Scenario A: "Scanning Mode" (0s - 15s)
Visual: Dashboard shows Green status "SCANNING SECTOR...".
Graph: Flat lines with minor thermal noise.
Action: Show the "Language Selector" in the sidebar to demonstrate Azure Translator changing the UI to Hindi/Spanish.
Scenario B: "Deep Signal Detected" (15s+)
Trigger: Automatically triggers after 150 packets (15 seconds).
Visual: Dashboard turns RED with "CRITICAL: RESPIRATION DETECTED".
Graph: Sine waves appear on the top chart.
Proof: The bottom FFT Graph shows a distinct spike at 0.25 Hz (Human Breathing Frequency).
Map: Azure Maps zooms into the Hanamkonda sector.

👥 Team
Team LifeSignal - Kamala Institute of Technology and Science
Lead Architect: Cloud Infrastructure & IoT
AI Research Lead: Signal Processing & ML Models
Embedded Systems: Hardware & Sensor Design
Product Strategy: B2G Business Model & UI/UX
📄 License
This project is submitted for the Microsoft Imagine Cup 2026.
Distributed under the MIT License. See LICENSE for more information.

