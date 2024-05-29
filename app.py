from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import time

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load CSV data, skipping the second row (index 1) which contains units
df = pd.read_csv("sample_vehicle_data_6kph.csv", skiprows=[1])

class DataItem(BaseModel):
    timestamps: float  # Treat timestamp as float
    latitude: float
    longitude: float
    spd_over_grnd: float  # Renamed speed over ground to spd_over_grnd

@app.get("/data", response_model=list[DataItem])
def get_data():
    # Add timestamp to each row of data
    data_with_timestamp = df.to_dict(orient="records")
    return data_with_timestamp

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
