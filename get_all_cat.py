#!/usr/bin/env python
import pywikibot
import csv
# import json


site = pywikibot.Site("en", "wiktionary")


def extractCatName(cat):
    title = cat
    return title.replace("Category:", "")

csvList = [['Title', 'ArticlesCount','isExtracted']]
pagesCount = 0
subcatsCount = 0
def main (catName = "Moroccan Arabic language"):
    cat = pywikibot.Category(site, catName)
    catInfo = cat.categoryinfo
    global subcatsCount
    global pagesCount
    pagesCount = catInfo["pages"]
    subcatsCount = catInfo["subcats"]
    print(pagesCount)

    
    if subcatsCount >=1:
        catList = list(cat.subcategories())
        for category in catList:
            name = extractCatName(category.title())
            if (not name.startswith("ary:") and not name.startswith('Moroccan Arabic terms belonging to the root')):
                if pagesCount >=1:
                    csvList.append([name, pagesCount, 'False'])
                    print("Category Name: " + str(name))
                main(name)

    # return csvList

# main()

with open('CategoryList.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    main() 
    writer.writerows(csvList)


