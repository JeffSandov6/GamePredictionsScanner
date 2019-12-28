from Websites.WinnersAndWhiners import WinnersAndWhiners

# first the input will ask for the sport, and the game

# we need to verify that this is an actual (upcoming) game 

# websitesMap = 

game = "Portland vs Ball State"
sport = "ncaab"


obj = WinnersAndWhiners(sport)


#make both teams lowercase and remove replace spaces w/ -

team1 = "niagara"
team2 = "syracuse"
obj.getPrediction(team1, team2)



