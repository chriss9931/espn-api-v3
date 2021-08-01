from league import League
from authorize import Authorize
from team import Team
from player import Player
from utils.building_utils import getUrl

import pandas as pd
import requests
from tabulate import tabulate as table

# Define user and season year
user_id = 'desi'
year = 2018

# Get login credentials for leagues
login = pd.read_csv('login.csv')
#_, username, password, league_id, swid, espn_s2 = login[login['id'] == user_id].values[0]

league_id = 1132847

# Generate cookies payload and API endpoint
# cookies = {'swid' : swid, 'espn_s2' : espn_s2}
url = getUrl(year, league_id)


league = League(league_id, year)
print(league)
