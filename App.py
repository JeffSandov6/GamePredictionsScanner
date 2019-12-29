from Websites.WinnersAndWhiners import WinnersAndWhiners

# first the input will ask for the 2 teams, and the sport
team1 = "niagara"
team2 = "syracuse"
sport = "ncaab"

# we need to verify that this is an actual (upcoming) game 

obj = WinnersAndWhiners(sport)

#make both teams lowercase and remove replace spaces w/ -

wwPredictions = obj.getPrediction(team1, team2)

print(wwPredictions)

# websitesMap = 








