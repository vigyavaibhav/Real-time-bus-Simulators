import time
import random

# Simple bus route with stops
bus_stops = ["Stop A", "Stop B", "Stop C", "Stop D", "Stop E"]

# Initialize bus position
bus_position = 0

print(" Real-Time Bus Tracker Simulator \n")
print("Route:", " -> ".join(bus_stops))
print("\nStarting journey...\n")

while bus_position < len(bus_stops):
    current_stop = bus_stops[bus_position]
    
    # Show current bus location
    print(f" Bus is at: {current_stop}")
    
    # Show next stop if available
    if bus_position < len(bus_stops) - 1:
        next_stop = bus_stops[bus_position + 1]
        eta = random.randint(2, 5)  # Random travel time in minutes
        print(f"➡ Next Stop: {next_stop} (ETA: {eta} minutes)\n")
    else:
        print(" Bus has reached the final stop!\n")
    
    # Wait a little before moving (simulate travel time)
    time.sleep(2)
    
    # Move bus forward
    bus_position +=1
