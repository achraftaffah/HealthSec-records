# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.controller import router as app_router
from py_eureka_client import eureka_client
import uvicorn

app = FastAPI()

# CORS settings
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router defined in controller.py
app.include_router(app_router)

# Run the FastAPI application with uvicorn
if __name__ == "__main__":
    eureka_client.init(eureka_server="http://localhost:8761", app_name="BasicDiseasePrediction-service", instance_port=8050)
    uvicorn.run("app:app", host="localhost", port=8083, reload=True)
