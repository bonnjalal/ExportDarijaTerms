import re
from regex_init import ReHelper
# import pprint


reH = ReHelper()

lng = "ary"


class AdvReg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################
    


    def extractVerb(self, wikiText):
    
        itemFrom = self.getAdverb(wikiText)

        return itemFrom

    #############################################

    # def getPlainLine(self, l):
    #     line = l
    #     line = reH.getSynonyms(line) 
    #     
    #     lbPatt = r'(?<={{lb\|'+lng+r'\|)(.*?)(?=}})'
    #     ux2Patt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
    #     ux1Patt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=\|)'
    #     # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'
    #
    #     lbMatchList = reH.reFindAll(lbPatt, l)
    #     uxMatch = reH.reFindFirst(ux1Patt, l)
    #     uxMatch2 = reH.reFindFirst(ux2Patt, l)
    #     # glossMatchList = reH.reFindAll(glossPatt, l)
    #     
    #     # print(line)
    #
    #     if len(lbMatchList) != 0:
    #         for m in lbMatchList:
    #             match = m
    #             match = match.replace('|', ', ')
    #             line = line.replace('{{lb|'+lng+'|'+ m +'}}', '(' + match + ')')
    #     
    #     if uxMatch != "":
    #         line = line.replace('{{ux|'+lng+'|'+ uxMatch2 +'}}', uxMatch)
    #     elif uxMatch2 != "":
    #         line = line.replace('{{ux|'+lng+'|'+ uxMatch2 +'}}', uxMatch2)
    #
    #         # print(uxMatchList)
    #         # for m in uxMatchList:
    #         #     line = line.replace('{{ux|'+lng+'|'+ m +'}}', match)
    #         
    #     
    #     # if len(glossMatchList) != 0:
    #     #     # print(uxMatchList)
    #     #     for m in glossMatchList:
    #     #         match = m
    #     #         line = line.replace('{{gloss|'+ m +'}}', match)
    #
    #
    #     linkPatt = r"\[\[(.*?)\]\]"
    #
    #     linkList = re.findall(linkPatt, line)
    #     for link in linkList:
    #         # print(link)
    #         if "|" in link:
    #             # print("true")
    #             findOr = reH.reFindFirst(r"^.*?\|", link)
    #             # print(findOr)
    #             line = line.replace("[[" +findOr, "")
    #         else:
    #             line = line.replace("[[" + link + "]]", link)
    #
    #     # newPattr = re.compile(r"\[\[(.*?)|")
    #     
    #     # line = re.sub(r'\[^\]\}]/g', '', line)
    #     # line = line.replace(']', '')
    #     # line = line.replace("{{ux|"+lng+"|", "")
    #     line = line.replace("'''", "")
    #     line = line.replace("''", "")
    #     line = line.replace("{{q|", "")
    #     line = line.replace("{{gloss|", "")
    #     line = line.replace("{{m|"+lng+"|", "")
    #     # line = re.sub(r'[^a-zA-Z0-9\'(),;.\s]', '',line)
    #     line = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF\'(),;.\s]', '',line)
    #     # print("AFTER: "+line)
    #
    #     return line
    #
   
    
    def getAdverb(self, txt):
        sectionDic = {}
        items = {}
        
        # text = '''_YES_ '''

        lines = txt.splitlines()
        

        # isline = False
        i = 0

        meaning = ""
        examplesList = []
        countExamples = 0

        hashtag1 = ""
        hashtag2 = ""
   
        hashtagCount = 0


        for x in range(len(lines)):
            l = lines[x]

            itemLen = len(items)

            if l.startswith('# '):
                # count1Hashtag += 1 
                if itemLen<i :
                    items.update({itemLen+1:{"meaning":meaning, "examples":examplesList }})
                    examplesList = []
                    meaning = ""


                line = reH.getPlainLine(l)
                hashtag1 = line
                meaning = line
                i+=1
                hashtagCount = 1
                # text += "\n" + line
            elif l.startswith('## '):
                if itemLen<i and hashtagCount != 1:
                    # if hashtagCount == 1:

                    items.update({itemLen+1:{"meaning":meaning, "examples":examplesList }})
                    examplesList = []
                    meaning = hashtag1

                    # print("itemsCount = " + str(len(items)) + " | i = " + str(i))
                
                line = reH.getPlainLine(l)
                hashtag2 = hashtag1 + line
                meaning += " " + line
                i+=1

                # isStartLine = False
                hashtagCount = 2
            elif l.startswith('### '):
                # if len(items)<i :
                if hashtagCount != 2:
                    items.update({itemLen+1:{"meaning":meaning, "examples":examplesList }})
                    examplesList = []
                    meaning = hashtag2

                line = reH.getPlainLine(l)
                meaning += " " + line
                i+=1
                hashtagCount = 3
            elif  l.startswith('#:') or l.startswith('##:') or l.startswith('###:'):
                countExamples += 1
                line = reH.getPlainLine(l)
                examplesList.append(line)

        if  len(items)<i :
            # items.update({i:{"meaning": meaning, "examples":examplesList}})
            items.update({len(items)+1:{"meaning":meaning, "examples":examplesList }})
            examplesList = []
            meaning = ""
            
        
        sectionDic.update(items)
 
        # fromDic.update({"Etymology": items})
        
        return sectionDic


text = """


"""
# myregl = myreg()
# getNoun = myregl.extractVerb(text)
#
# print(getNoun)
