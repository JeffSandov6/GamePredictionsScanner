import requests
import bs4
from lxml import html

class SportsChatPlace:

    sportWebsiteMap = {
        "siteHomePage" : "https://sportschatplace.com/",
        "ncaab" : "https://sportschatplace.com/college-basketball-picks/",
        "nfl" : "https://sportschatplace.com/nfl-picks/", #might change this to todays-games
        "nba" : "https://sportschatplace.com/nba-picks/"
    }

    def __init__(self, sport):
        self.currentSportWebsite = self.sportWebsiteMap[sport]
        self.pageRequest = requests.get(self.currentSportWebsite)
        self.pageTree = html.fromstring(self.pageRequest.content)


    def getPrediction(self, team1, team2):
        predictionSiteLink = self.getPredictionSiteLink(team1, team2)
        if not predictionSiteLink:
            return "Couldn't find any predictions"

        predictions = self.getAllAvailablePredictions(predictionSiteLink)

        return predictions

    def getPredictionSiteLink(self, team1, team2):
        rowOfGamesElem = self.pageTree.xpath('//*[@id="content"]/div/section/div[3]')
        potentialGameLinks = set()

        for x in rowOfGamesElem:
            links = x.iterlinks()

            for i in links:
                if (team1 in i[2]) or (team2 in i[2]):
                    potentialGameLinks.add(i[2])


        if(len(potentialGameLinks) > 1 or len(potentialGameLinks) < 1):
            return ""

        return self.structureLink(potentialGameLinks.pop())

    def structureLink(self, gameLink):
        return self.sportWebsiteMap["siteHomePage"] + gameLink

    
    def getAllAvailablePredictions(self, predictionSiteLink):
        pageRequest = requests.get(predictionSiteLink)
        pageTree = html.fromstring(pageRequest.content)

        pickClassElemList = pageTree.find_class("article-pick")
        pickClassElemList = pickClassElemList[0].xpath('div/div/div/div[2]/h3/span[2]')
    

        predictions = []
        for curElem in pickClassElemList:
            predictions.append(curElem.text)

        return predictions











