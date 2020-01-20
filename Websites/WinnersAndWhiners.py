import requests
import bs4
from lxml import html

class WinnersAndWhiners:

    sportWebsiteMap = {
        "siteHomePage" : "http://winnersandwhiners.com/",
        "ncaab" : "https://winnersandwhiners.com/games/ncaab",
        "nfl" : "https://winnersandwhiners.com/games/nfl/",
        "nba" : "https://winnersandwhiners.com/games/nba/"
    }

    def __init__(self, sport):
        self.currentSportWebsite = self.sportWebsiteMap[sport]
        self.pageRequest = requests.get(self.currentSportWebsite)
        self.pageTree = html.fromstring(self.pageRequest.content)

    def getPrediction(self, team1, team2):
        predictionSiteLink = self.getPredictionSiteLink(team1, team2)

        if not predictionSiteLink: #if no links for this game are found
            return "Not a valid game"
        
        predictions = self.getAllAvailablePredictions(predictionSiteLink)

        return predictions #right now, returning a list of all predictions

    
    def getAllAvailablePredictions(self, predictionSiteLink):
        pageRequest = requests.get(predictionSiteLink)
        pageTree = html.fromstring(pageRequest.content)

        # temp = pageTree.xpath('//*[@id="full-game-side"]') #correct one 
        # temp = pageTree.get_element_by_id("full-game-side")

        pickClassElemList = pageTree.find_class("pick") #this finds all classes named pick and returns a list of its elements
        predictions = []
        for curElem in pickClassElemList:
            parent = curElem.getparent()
            currentBetType = parent.attrib['id']  #returns the bet type

            for curPrediction in curElem.getchildren():
                prediction = curPrediction.text.replace('Prediction', currentBetType)

                # predictions.append(curPrediction.text)
                predictions.append(prediction.strip())

        return predictions

    
    def getPredictionSiteLink(self, team1, team2):
        rowOfGamesElem = self.pageTree.xpath('//*[@id="ww-vue-app"]/div[3]/div/div[2]/div[2]/div') #returns elems after div class="row"
        potentialGameLinks = set()

        for x in rowOfGamesElem:
            links = x.iterlinks()
            for i in links:
                #the way the links object is returned, each object has 4 parts to it,
                #where the second is the link
                if (team1 in i[2]) and (team2 in i[2]) and (i[2][0:5] == "https"):
                    potentialGameLinks.add(i[2])

        return self.getCorrectLink(potentialGameLinks)



    def getCorrectLink(self, potentialGameLinks):
        correctLink = ""
        for gameLink in potentialGameLinks:
            if(self.hasCorrectFormat(gameLink)):
                correctLink = gameLink
                break

        return correctLink

    def hasCorrectFormat(self, gameLink):
        firstDateNum = gameLink[42:43] #gets the first char right after ncaab/ in the link
        return firstDateNum.isnumeric() #if its a number (part of a date), this is the correct link
