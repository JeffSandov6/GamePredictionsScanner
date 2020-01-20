import requests
import bs4
from lxml import html

class StatSalt:

    sportWebsiteMap = {
        "siteHomePage" : "https://statsalt.com/",
        "ncaab" : "https://statsalt.com/games/ncaab/",
        "nfl" : "https://statsalt.com/games/nfl/",
        "nba" : "https://statsalt.com/games/nba/"
    }

    def __init__(self, sport):
        self.currentSportWebsite = self.sportWebsiteMap[sport]
        self.pageRequest = requests.get(self.currentSportWebsite)
        self.pageTree = html.fromstring(self.pageRequest.content)

    
    def getPrediction(self, team1, team2):
        predictionSiteLink = self.getPredictionSiteLink(team1, team2)

        if not predictionSiteLink:
            return "Not a valid game"

        predictions = self.getAllAvailablePredictions(predictionSiteLink)

        return predictions


    def getPredictionSiteLink(self, team1, team2):
        rowOfGamesElem = self.pageTree.xpath('//*[@id="cards"]')
        #it seems that this set isnt needed here because only 1 link per team is being found
        # potentialGameLinks = set()

        correctLink = ""
        
        for x in rowOfGamesElem:
            links = x.iterlinks()

            for i in links:
                if (team1 in i[2]) and (team2 in i[2]) and (i[2][0:5] == "https"):
                    correctLink = i[2]
                    break

        return correctLink

    
    def getAllAvailablePredictions(self, predictionSiteLink):
        pageRequest = requests.get(predictionSiteLink)
        pageTree = html.fromstring(pageRequest.content)
        
        #this finds all div classes named "pick" and returns a list of its children element
        pickClassElemList = pageTree.find_class("pick")
        predictions = []

        #we have to go 2 layers of children down for this website, to find the actual predictions
        for curElem in pickClassElemList:
            parent = curElem.getparent()
            currentBetType = parent.find('h5').text # returns the bet type
            
            for curPrediction in curElem.getchildren():
                for curPredChild in curPrediction.getchildren():
                    prediction = currentBetType + ': ' + curPredChild.text
                    predictions.append(prediction.strip().lower())
        
        return predictions
