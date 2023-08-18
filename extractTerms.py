#!/usr/bin/env python
import pywikibot
import requests
import json


def getSecInfo(secDict, line):
    for x in secDict["parse"]["sections"]:
        if x["line"] == line:
            return x["index"], x["number"]
    return "-1.0","-1.0"


def getAllSect(secDict, startNum):
    startNum += "."
    sections = {}
    for x in secDict["parse"]["sections"]:
        num = x["number"]
        if num.startswith(startNum):
            sections[num] = x["index"]
    return sections


site = pywikibot.Site("en", "wiktionary")
#user = pywikibot.User(site, "Bonnjalal00")
#cat = pywikibot.Category(site, "Moroccan Arabic templates")
cat = pywikibot.Category(site, "Moroccan Arabic language")
#mem = cat.members()

#for user in range(10):
#    print (list(allusers).get(user))

catInfo = cat.categoryinfo

pagesCount = catInfo["pages"]
subcatsCount = catInfo["subcats"]


#print(type(pagesCount))
#print(subcatsCount)

print(cat.categoryinfo)
catList = list(cat.subcategories())
#print(catList)
title = list(catList[0].articles())[7].title()
print(title)

sectionsJson = requests.get("https://en.wiktionary.org/w/api.php?action=parse&prop=sections&page={}&format=json".format(title))
sectionsDict = sectionsJson.json()
secIndex, secNum = getSecInfo(sectionsDict,"Moroccan Arabic") 

allSections = getAllSect(sectionsDict, secNum)
#selectedSectJson = requests.get("https://en.wiktionary.org/w/api.php?action=parse&prop=wikitext&section={}&page={}&format=json".format(secIndex,title))
#sectionText = selectedSectJson.json()

## count char in a string ##
#string.count('.')

# text = list(catList[0].articles())[0].text
# print(sectionsDict["parse"]["sections"][17])

for num, index in allSections.items():
    print(num,index)
    selectedSectJson = requests.get("https://en.wiktionary.org/w/api.php?action=parse&prop=wikitext&section={}&page={}&format=json".format(index,title))
    sectionText = selectedSectJson.json()
    print(sectionText["parse"]["wikitext"])
    print(num.count("."))
print(allSections)


## convert json to xlxs (needs to convert dict to json first)
# import  jpype     
#   import  asposecells     
#   jpype.startJVM() 
#   from asposecells.api import Workbook
#   workbook = Workbook("testData.json")
#   workbook.save("testData.xlsx")
#   jpype.shutdownJVM()

