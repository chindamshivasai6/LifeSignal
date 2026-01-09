import csv
import math
import random
import os

print("🚀 STARTING DATA GENERATION...")

def generate_file(filename, mode='empty'):
    print(f"   ... Writing {filename}")
    data = []
    # 60 seconds @ 10Hz = 600 samples
    for t in range(600):
        timestamp = t / 10
        # Base noise (thermal/environment)
        noise = random.gauss(0, 0.2)
        
        if mode == 'human':
            # Sensor A: Strong signal (closer to victim)
            # Formula: Base + Sine Wave (0.25Hz) + Noise
            signal = 45.0 + (math.sin(2 * math.pi * 0.25 * timestamp) * 5.0) + noise
        elif mode == 'human_weak':
            # Sensor B: Weaker signal (further away)
            signal = 42.0 + (math.sin(2 * math.pi * 0.25 * timestamp) * 3.0) + noise
        elif mode == 'human_lag':
            # Sensor C: Slight phase shift (different angle)
            signal = 44.0 + (math.sin(2 * math.pi * 0.25 * (timestamp - 0.5)) * 4.5) + noise
        elif mode == 'rat':
            # Rat: Fast twitchy signal (1.5Hz)
            signal = 45.0 + (math.sin(2 * math.pi * 1.5 * timestamp) * 2.0) + noise
        else:
            # Rubble: Just noise
            signal = 40.0 + noise
            
        data.append(round(signal, 4))

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for val in data: writer.writerow([val])
    print(f"✅ SUCCESS: {filename}")

if __name__ == "__main__":
    generate_file('data_rubble.csv', mode='empty')
    generate_file('data_human_A.csv', mode='human')      # Sensor 1
    generate_file('data_human_B.csv', mode='human_weak') # Sensor 2
    generate_file('data_human_C.csv', mode='human_lag')  # Sensor 3
    print("\n🎉 DATA GENERATION COMPLETE. READY FOR SENSORS.")