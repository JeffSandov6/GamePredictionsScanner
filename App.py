from Websites.WinnersAndWhiners import WinnersAndWhiners
from Websites.StatSalt import StatSalt


def removeSpacesInTeamNames(teamName):
    teamName = teamName.strip()
    return teamName.replace(" ", "-")


def getPredictionsFromSites(team1, team2, sport):
    wwObj = WinnersAndWhiners(sport)
    statSaltObj = StatSalt(sport)

    listOfLists = []

    wwPredictions = wwObj.getPrediction(team1, team2)
    # this will be the check for whether or not the user is looking for a valid game, that way, 
    # we won't check the other sites for their predictions, thus saving resources
    if(wwPredictions == 'Not a valid game'):
        print("This is not a valid game")
        return
    

    statSaltPredictions = statSaltObj.getPrediction(team1, team2)


    listOfLists.append((wwObj.sportWebsiteMap['siteHomePage'], wwPredictions))
    listOfLists.append((statSaltObj.sportWebsiteMap['siteHomePage'], statSaltPredictions))


    printPredictions(listOfLists)






def printPredictions(listOfObjectsAndPredictions):
    for (homeLink, sitePredictionsList) in listOfObjectsAndPredictions:
        print("Predictions from " + homeLink + " are: ")

        for curPrediction in sitePredictionsList:
            print(curPrediction)

        print()



team1 = "oklahoma"
team2 = "baylor"
sport = "ncaab"

# team1 = removeSpacesInTeamNames(
#     input("What's the first team's name? ").lower())
# team2 = removeSpacesInTeamNames(
#     input("What's the second team's name? ").lower())
# sport = input("Choose 1 of the following sports: ncaab, nfl, nba: ").lower().strip()

print()


getPredictionsFromSites(team1, team2, sport)






    




