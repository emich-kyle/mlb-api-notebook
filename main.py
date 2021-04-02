pip install MLB-StatsAPI

import statsapi

longest_team_name = max([x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']],key=len)
print('The team with the longest name is %s, at %s characters.' % (longest_team_name, len(longest_team_name)))

players_list = [x['name'] for x in statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name'})['teams']]
print(players_list)
