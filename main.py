#in order to get more complete data, I have used the MLB-StatsAPI on a Jupyter notebook to make better player lists.
#this is easier to do in Python. now, the true player positions are included in the .json files among other fields.
#i will need to refactor the main class to have a Hitter class that extends Player and a Pitcher class that extends Player
#and i will need to implement some external json library for Java in order to parse the relevant data into objects
#because our data will no longer use .csv files; instead, it will use .json files
#this python code can be run in an online Jupyter notebook for testing but that won't be necessary since
#i have already extracted the data into .json files with it

#kyle

pip install MLB-StatsAPI

import statsapi

#test
longest_team_name = max([x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']],key=len)
print('The team with the longest name is %s, at %s characters.' % (longest_team_name, len(longest_team_name)))

#test
players_list = [x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']]
print(players_list)

#test
players_list = statsapi.get('sports_players',{'season':2019,'gameType':'R'})['people']
player_ids = []
for player in players_list:
    player_ids.append(player['id'])   
print(player_ids)  ##ok here we go, all player ids for 2019 season

import json

#test one player
with open("test.json", "w") as write_file:
    json.dump(statsapi.player_stat_data(650556, group="[hitting]", type="yearByYear"), write_file)
    
#For player objects
with open("new_players_list.json", "w") as write:
    json.dump(players_list, write)
    
#For hitter objects
hitting_list = []
for player in players_list:
    r = statsapi.player_stat_data(player['id'], group="[hitting]", type="yearByYear")
    hitting_list.append(r)

with open("new_hitting_list.json", "w") as write:
    json.dump(hitting_list, write)

#For pitcher objects
pitching_list = []
for player in players_list:
    r = statsapi.player_stat_data(player['id'], group="[pitching]", type="yearByYear")
    pitching_list.append(r)

with open("new_pitching_list.json", "w") as write:
    json.dump(pitching_list, write)

