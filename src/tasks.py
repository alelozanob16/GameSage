from crewai import Task
from src.agents import vg_researcher, vg_referrer, serper_tool

# Define the task
research_task = Task(
    description="""
    You must research the most related information information about video games based on {query}.
    You must extract all the relevant information in order to help the Referrer agent to refer the best video games to the user.
    It must be 
    """,
    agent = vg_researcher,
    expected_output = "A highly detailed report in markdown.",
    output_file='./output/research-output.md',
    tools = [serper_tool]
)

referral_task = Task(
    description="""
    You must refer the best video games based on the information provided by the Researcher agent which is based on the previous task(reserach_task).
    You must extract all the relevant information from the news that the researches has provided you in order to help the user to choose the best video game for him and tell why you have chosen these video games 
    and why you think user will like them.
    """,
    agent = vg_referrer,
    expected_output = "An organized md in which the info can be cleared read.",
    output_file='./output/referer-output.md'
)