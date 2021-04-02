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
    hitting_list.append(r)

with open("new_pitching_list.json", "w") as write:
    json.dump(pitching_list, write)

