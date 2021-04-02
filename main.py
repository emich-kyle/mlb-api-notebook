pip install MLB-StatsAPI

import statsapi

longest_team_name = max([x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']],key=len)
print('The team with the longest name is %s, at %s characters.' % (longest_team_name, len(longest_team_name)))

players_list = [x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']]
print(players_list)

players_list = statsapi.get('sports_players',{'season':2019,'gameType':'R'})['people']
player_ids = []
for i in players_list:
    player_ids.append(i['id'])
    
print(player_ids)  ##ok here we go all player ids for 2019 season

import json

players_list = statsapi.get('sports_players',{'season':2019,'gameType':'R'})['people']

with open("test.json", "w") as write_file:
    json.dump(statsapi.player_stat_data(650556, group="[hitting]", type="yearByYear"), write_file)

hitting_list = []
for player in players_list:
    r = statsapi.player_stat_data(player['id'], group="[hitting]", type="yearByYear")
    hitting_list.append(r)

with open("new_hitting_list.json", "w") as write:
    json.dump(hitting_list, write)


