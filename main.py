import os
from os import path
from datetime import datetime
from team import Team
files = list(filter(path.isfile, os.listdir('./')))
filename = 'top3list.csv'
delim = '+'
x = 0
y = 0
z = 0
teams = []

print
while x < len(files):
	if files[x] == filename:
		print('Filename: ' + files[x])
		print('Modified At: ' + datetime.fromtimestamp(os.path.getctime('./' + files[x])).strftime('%Y-%m-%d %H:%M %p'))
	x += 1

with open(filename) as f:
	content = f.readlines()

content = [x.strip() for x in content] 
while y < len(content):
	t1 = content[y].split(',', 1)[0]
	t2 = content[y].split(',', 1)[1]
	teams.append(Team(t1, t2))
	y += 1
print

while z < len(teams):
	s = len('| Team: ' + teams[z].name + ' |') - 2
	print(delim + ('-' * s) + delim)
	print('| Team: ' + teams[z].name + ' |')
	s2 = len('| Super Bowl Wins: ' + teams[z].super_bowl_wins)
	print('| Super Bowl Wins: ' + teams[z].super_bowl_wins + (' ' * (s - s2)) + ' |')
	print(delim + ('-' * s) + delim)
	print
	z += 1
