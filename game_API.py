from src.crew_main import run_crew_game_recommendations
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/games/{query}")
def game_recommend(query: str):
    gr = run_crew_game_recommendations(query)
    return JSONResponse(content = gr)
