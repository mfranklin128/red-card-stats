import csv, sys, operator

reader = csv.DictReader(open(sys.argv[1]))

total_reds_in_game = {}

for row in reader:
	home_team = row["HomeTeam"]
	away_team = row["AwayTeam"]
	home_red = row["HR"]
	away_red = row["AR"]

	if home_team in total_reds_in_game:
		total_reds_in_game[home_team] += int(home_red) + int(away_red)
	else:
		total_reds_in_game[home_team] = int(home_red) + int(away_red)

	if away_team in total_reds_in_game:
		total_reds_in_game[away_team] += int(home_red) + int(away_red)
	else:
		total_reds_in_game[away_team] = int(home_red) + int(away_red)

#for (key, val) in sorted(total_reds_in_game.items(), reverse=True, key=operator.itemgetter(1)):
#	print "%s, %d" % (key, val)

print ",".join([str(x) for x in total_reds_in_game.values()])
