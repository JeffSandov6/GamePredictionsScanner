from Websites.WinnersAndWhiners import WinnersAndWhiners
from Websites.StatSalt import StatSalt
from Websites.SportsChatPlace import SportsChatPlace


def removeSpacesInTeamNames(teamName):
    teamName = teamName.strip()
    return teamName.replace(" ", "-")


def getPredictionsFromSites(team1, team2, sport):
    wwObj = WinnersAndWhiners(sport)
    statSaltObj = StatSalt(sport)
    scpObj = SportsChatPlace(sport)


    listOfLists = []

    wwPredictions = wwObj.getPrediction(team1, team2)
    statSaltPredictions = statSaltObj.getPrediction(team1, team2)
    scpPredictions = scpObj.getPrediction(team1, team2)

    if isinstance(wwPredictions, str) and isinstance(statSaltPredictions, str) and isinstance(scpPredictions, str):
        print("Not a valid game, or no predictions have been posted.")
        return


    listOfLists.append((wwObj.sportWebsiteMap['siteHomePage'], wwPredictions))
    listOfLists.append((statSaltObj.sportWebsiteMap['siteHomePage'], statSaltPredictions))
    listOfLists.append((scpObj.sportWebsiteMap['siteHomePage'], scpPredictions))


    printPredictions(listOfLists)






def printPredictions(listOfObjectsAndPredictions):
    for (homeLink, sitePredictionsList) in listOfObjectsAndPredictions:
        print("Predictions from " + homeLink + " are: ")
        
        if isinstance(sitePredictionsList, str):
            print("No predictions found")
            print()
            continue

        for curPrediction in sitePredictionsList:
            print(curPrediction)

        print()



# team1 = "lakers"
# team2 = "celtics"
# sport = "nba"

team1 = removeSpacesInTeamNames(
    input("What's the first team's name? ").lower())
team2 = removeSpacesInTeamNames(
    input("What's the second team's name? ").lower())
sport = input("Choose 1 of the following sports: ncaab, nfl, nba: ").lower().strip()

print()


getPredictionsFromSites(team1, team2, sport)


# print(scpPredictions)






    




