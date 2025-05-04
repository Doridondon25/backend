from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from firebase_funcs import set_ECG, set_humidity, set_temperature, set_bpm, get_direction, update_all
from dotenv import load_dotenv

# load_dotenv("/etc/secrets/")

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    data: int

class AllData(BaseModel):
    temperature: int
    humidity: int
    ecg: int
    bpm: int

@app.get("/")
async def root():
    return {"message": "server is working"}


@app.post("/set-ecg")
async def set_ecg(data: Data):
    set_ECG(data.data)
    return {"message": "ECG set"}

@app.post("/set-humidity")
async def set_humidity(data: Data):
    set_humidity(data.data)
    return {"message": "humidity set"}

@app.post("/set-temperature")
async def set_temperature(data: Data):
    set_temperature(data.data)
    return {"message": "temperature set"}

@app.post("/set-bpm")
async def set_bpm(data: Data):
    set_bpm(data.data)
    return {"message": "bpm set"}


@app.get("/get-robot-direction")
async def get_robot_direction():
    direction = await get_direction()
    return {"direction": direction}


@app.post("/update-all-values")
async def update_all_values(data: AllData):
    update_all(data.temperature, data.humidity, data.ecg, data.bpm)
    return {"message": "all values updated"}