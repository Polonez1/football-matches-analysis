import logging
import sys

# URL
MATCHES_URL = "https://api.football-data-api.com/league-matches?key={api_token}&season_id={season_id}"
TEAMS_URL = "https://api.football-data-api.com/league-teams?key={api_token}&season_id={season_id}&include=stats"

# logging
log = logging.basicConfig(stream=sys.stdout, level=logging.INFO)
