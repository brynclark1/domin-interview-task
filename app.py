from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
import threading
import time

app = FastAPI()

# Allows API to interact with ReactJS App
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Buffer to store CSV data
buffer = {
    "data": [],
    "timestamps": 0
}
buffer_refresh_interval = 1  # Refresh buffer every second
csv_file = 'sample_vehicle_data_6kph.csv'

def refresh_buffer():
    while True:
        df = pd.read_csv(csv_file, skiprows=[1])
        buffer["data"] = df.to_dict(orient="records")
        time.sleep(buffer_refresh_interval)

# Start a thread to refresh the buffer periodically
threading.Thread(target=refresh_buffer, daemon=True).start()

# /data endpoint
@app.get("/data")
async def get_data():
    return buffer["data"]

# /data-range endpoint for querying time data range
@app.get("/data-range")
async def get_data_range(
    start_time: float = Query(..., description="Start time in seconds"),
    end_time: float = Query(..., description="End time in seconds")
):
    if start_time > end_time:
        raise HTTPException(status_code=400, detail="start_time must be less than end_time")

    # Filter data within the specified time range
    filtered_data = [item for item in buffer["data"] if start_time <= item["timestamps"] <= end_time]
    return filtered_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
