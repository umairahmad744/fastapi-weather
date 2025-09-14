from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Weather API is running 🚀"}

@app.get("/weather/{city}")
def get_weather(city: str):
    return {"city": city, "temperature": "28°C", "condition": "Sunny"}
