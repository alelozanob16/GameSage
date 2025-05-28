from crewai import Agent
from crewai import LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os
load_dotenv()


llm = LLM(
    model = "openrouter/deepseek/deepseek-prover-v2:free",
    base_url = "https://openrouter.ai/api/v1",
    temperature = 0.8,
    api_key = os.getenv("OPENROUTER_API_KEY")
)

serper_tool = SerperDevTool(
    api_key = os.getenv("SERPER_API_KEY"),
    search_engine = "google",
    search_type = "search"
)

vg_researcher = Agent(
    role = "Researcher",
    goal = "Research info about video games on the internet.",
    backstory = "You are an specialist reseacher in video games, focused on the latest news and trends.",
    tools = [serper_tool],
    llm = llm
)

vg_referrer = Agent(
    role = "Referrer",
    goal = "Refers the best video games to the user.",
    backstory = "You are a video game expert, and you know the best games for each type of player.",
    llm = llm
)