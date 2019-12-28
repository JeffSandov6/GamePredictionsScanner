import requests
import bs4
from lxml import html

class WinnersAndWhiners:

    sportWebsiteMap = {
        "ncaab" : "https://winnersandwhiners.com/games/ncaab"
    }

    # currentSportWebsite = ""

    def __init__(self, sport):
        self.currentSportWebsite = self.sportWebsiteMap[sport]
        self.pageRequest = requests.get(self.currentSportWebsite)
        self.pageTree = html.fromstring(self.pageRequest.content)

    def getPrediction(self, team1, team2):
        predictionSiteLink = self.getPredictionSiteLink(team1, team2)
        print(predictionSiteLink)

        pageRequest = requests.get(predictionSiteLink)
        pageTree = html.fromstring(self.pageRequest.content)

    
    def getPredictionSiteLink(self, team1, team2):
        rowOfGamesElem = self.pageTree.xpath('//*[@id="ww-vue-app"]/div[3]/div/div[2]/div[2]/div') #returns elems after div class="row"

        potentialGameLinks = set() #this should be a set
        # someLinks = []
        for x in rowOfGamesElem:
            links = x.iterlinks()

            for i in links:
                if team1 in i[2] and i[2][0:5] == "https":
                    potentialGameLinks.add(i[2])
                    # someLinks.append(i[2])

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




########################################

            # next = x.find_class("title")

            # print("the type is")
            # print(type(next))
            
            # for i in next:
            #     try:
            #         print(i.text_content())
            #     except:
            #         print("skipping the ones w out it")


            