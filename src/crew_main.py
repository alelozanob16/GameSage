from dotenv import load_dotenv
load_dotenv()
from langtrace_python_sdk import langtrace
import os

from crewai import Crew, Process, Agent, Task,TaskOutput, CrewOutput
from src.agents import vg_researcher, vg_referrer
from src.tasks import research_task, referral_task


def run_crew_game_recommendations(query, verbose = True):
    api_key = os.getenv("LANGTRACE_API_KEY")
    if not api_key:
        raise ValueError("LANGTRACE_API_KEY environment variable is not set.")
    langtrace.init(api_key = api_key)
    report_crew = Crew(
        agents = [vg_researcher, vg_referrer],
        tasks = [research_task, referral_task],
        process = Process.sequential,
        verbose = verbose
    )

    result = report_crew.kickoff(inputs = {"query": query})

    crew_output = result.raw

    return crew_output