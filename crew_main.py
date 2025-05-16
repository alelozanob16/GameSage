from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process, Agent, Task,TaskOutput, CrewOutput
from src.agents import vg_researcher, vg_referrer
from src.tasks import research_task, referral_task

query = "Lately I've been playing a lot of rpg games and I love when they got a deep story so what do you think should I play next"

run_crew_game_recommendations(query)


def run_crew_game_recommendations(query, verbse = False):
    report_crew = Crew(
        agents = [vg_researcher, vg_referrer],
        tasks = [research_task, referral_task],
        proccess = Proccess.sequential,
        verbose = verbse
    )

    result = report_crew.kickoff(inputs = {"query": query})

    crew_output = result.raw

    return crew_output


