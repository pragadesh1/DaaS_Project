import random
import time
import requests
import os

# InfluxDB Configuration from Environment Variables
INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")

def read_moisture_sensor():
    return random.randint(0, 539)

def calculate_moisture_percentage(moisture_value):
    return (moisture_value / 539.0) * 100

def write_to_influxdb(measurement, moisture_value, moisture_percentage):
    data = f"{measurement},location=garden moisture_value={moisture_value},moisture_percentage={moisture_percentage:.2f}"
    url = f"{INFLUXDB_URL}/api/v2/write?org={INFLUXDB_ORG}&bucket={INFLUXDB_BUCKET}&precision=s"
    headers = {"Authorization": f"Token {INFLUXDB_TOKEN}", "Content-Type": "text/plain"}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 204:
        print("Data written successfully.")
    else:
        print(f"Failed to write data: {response.status_code}, {response.text}")

def main():
    try:
        while True:
            moisture_value = read_moisture_sensor()
            moisture_percentage = calculate_moisture_percentage(moisture_value)
            print(f"Moisture Value: {moisture_value}, Moisture Percentage: {moisture_percentage:.2f}%")
            write_to_influxdb("soil_moisture", moisture_value, moisture_percentage)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopping data collection.")

if __name__ == "__main__":
    main()
