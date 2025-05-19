from crew_main import run_crew_game_recommendations
from src.agents import vg_researcher, vg_referrer
from src.tasks import research_task, referral_task

query = "Lately I've been playing rpg games, What rpg games would you recommend me based on the last games I've played are Baldurs Gate 3 and Oblivion"
run_crew_game_recommendations(query, verbose = True)cls