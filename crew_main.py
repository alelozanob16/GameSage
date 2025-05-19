from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process, Agent, Task,TaskOutput, CrewOutput
from src.agents import vg_researcher, vg_referrer
from src.tasks import research_task, referral_task

def run_crew_game_recommendations(query, verbose = True):
    report_crew = Crew(
        agents = [vg_researcher, vg_referrer],
        tasks = [research_task, referral_task],
        process = Process.sequential,
        verbose = verbose
    )

    result = report_crew.kickoff(inputs = {"query": query})

    crew_output = result.raw

    return crew_output


