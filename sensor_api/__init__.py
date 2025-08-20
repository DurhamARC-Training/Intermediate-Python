"""
Virtual Sensor API Module
This module simulates a plant monitoring sensor.
"""

import random
import time

# Global state to track connections
_connected_sensors = set()

def connect(sensor_id: str) -> bool:
    """
    Connect to a sensor with given ID.
    Returns True if successful, False otherwise.
    """
    if sensor_id in _connected_sensors:
        print(f"Sensor {sensor_id} is already connected!")
        return False
    
    _connected_sensors.add(sensor_id)
    print(f"Sensor {sensor_id} connected successfully.")
    return True

def disconnect(sensor_id: str) -> bool:
    """
    Disconnect a sensor with given ID.
    Returns True if successful, False otherwise.
    """
    if sensor_id not in _connected_sensors:
        print(f"Sensor {sensor_id} is not connected!")
        return False
    
    _connected_sensors.remove(sensor_id)
    print(f"Sensor {sensor_id} disconnected.")
    return True

def send_message(message: str) -> str | None:
    """
    Send a message to the sensor and get a reading.
    Message format: "SENSOR_ID:COMMAND"
    Commands: SOIL_HUMIDITY, AIR_HUMIDITY, TEMPERATURE
    Returns the reading value or None if error.
    """
    try:
        sensor_id, command = message.split(":")
        
        if sensor_id not in _connected_sensors:
            print(f"Error: Sensor {sensor_id} is not connected!")
            return None
        
        # Simulate sensor readings
        if command == "SOIL_HUMIDITY":
            return str(round(random.uniform(20, 80), 1))  # percentage
        elif command == "AIR_HUMIDITY":
            return str(round(random.uniform(30, 70), 1))  # percentage
        elif command == "TEMPERATURE":
            return str(round(random.uniform(15, 30), 1))  # Celsius
        else:
            print(f"Unknown command: {command}")
            return None
            
    except ValueError:
        print("Invalid message format! Use 'SENSOR_ID:COMMAND'")
        return None