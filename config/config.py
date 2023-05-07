import logging
import sys
import os

# URL
MATCHES_URL = "https://api.football-data-api.com/league-matches?key={api_token}&season_id={season_id}"
TEAMS_URL = "https://api.football-data-api.com/league-teams?key={api_token}&season_id={season_id}&include=stats"

# logging
log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# path

CURRENT_PATH = os.path.abspath(__file__)
PROJECT_PATH = os.path.dirname(os.path.dirname(CURRENT_PATH))
