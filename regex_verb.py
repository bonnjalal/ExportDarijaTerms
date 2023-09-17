import re
from regex_init import ReHelper
# import pprint


reH = ReHelper()

lng = "ary"


class VerbReg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################
    


    def extractVerb(self, wikiText):
    
        itemFrom = self.getVerb(wikiText)

        return itemFrom

    #############################################

    def getPlainLine(self, l):
        line = l
        lbPatt = r'(?<={{lb\|'+lng+r'\|)(.*?)(?=}})'
        # uxPatt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
        # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'

        lbMatchList = reH.reFindAll(lbPatt, l)
        # uxMatchList = reH.reFindAll(uxPatt, l)
        # glossMatchList = reH.reFindAll(glossPatt, l)
        
        # print(line)

        if len(lbMatchList) != 0:
            for m in lbMatchList:
                match = m
                match = match.replace('|', ', ')
                line = line.replace('{{lb|'+lng+'|'+ m +'}}', '(' + match + ')')
        
        # if len(uxMatchList) != 0:
        #     # print(uxMatchList)
        #     for m in uxMatchList:
        #         match = m
        #         line = line.replace('{{ux|'+lng+'|'+ m +'}}', match)
        
        # if len(glossMatchList) != 0:
        #     # print(uxMatchList)
        #     for m in glossMatchList:
        #         match = m
        #         line = line.replace('{{gloss|'+ m +'}}', match)


        linkPatt = r"\[\[(.*?)\]\]"

        linkList = re.findall(linkPatt, line)
        for link in linkList:
            # print(link)
            if "|" in link:
                # print("true")
                findOr = reH.reFindFirst(r"^.*?\|", link)
                # print(findOr)
                line = line.replace("[[" +findOr, "")
            else:
                line = line.replace("[[" + link + "]]", link)

        # newPattr = re.compile(r"\[\[(.*?)|")
        
        # line = re.sub(r'\[^\]\}]/g', '', line)
        # line = line.replace(']', '')
        line = line.replace("{{ux|"+lng+"|", "")
        line = line.replace("'''", "")
        line = line.replace("''", "")
        line = line.replace("{{q|", "")
        line = line.replace("{{gloss|", "")
        line = line.replace("{{m|"+lng+"|", "")
        line = re.sub(r'[^a-zA-Z0-9\'(),;.\s]', '',line)
        # print("AFTER: "+line)

        return line


    def getVerb(self, txt):
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


                line = self.getPlainLine(l)
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
                
                line = self.getPlainLine(l)
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

                line = self.getPlainLine(l)
                meaning += " " + line
                i+=1
                hashtagCount = 3
            elif  l.startswith('#:') or l.startswith('##:') or l.startswith('###:'):
                countExamples += 1
                line = self.getPlainLine(l)
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
====Verb====
{{en-verb}}

# {{lb|en|chiefly|transitive}} To [[give birth]] to or [[produce]] (as its female parent) a [[child]]. {{q|Compare ''[[father#Verb|father]]''.}}
#* {{quote-book
|en
|year=1998
|author=Nina Revoyr
|title=The Necessary Hunger: A Novel
|publisher=Macmillan
|isbn=9780312181420
|page=101
|passage=Q's sister, Debbie, had '''mothered''' two kids by the time she was twenty, with neither of the fathers in sight.}}
#* {{quote-book
|en
|year=2010
|author=Lynette Joseph-Bani
|title=The Biblical Journey of Slavery: From Egypt to the Americas
|publisher=AuthorHouse
|isbn=9781452009070
|page=51
|passage=Zilpah, Leah's maid, '''mothered''' two sons for Jacob, Gad and Asher. Leah became pregnant once more and had two more sons, Issachar, and Zebulun, and a daughter, Dinah, thus Leah had seven children for Jacob.}}
# {{lb|en|transitive}} To treat as a mother would be expected to treat her child; to [[nurture]].
#* {{quote-text|en|year=c. 1900|author=w:O. Henry|title=s:An Adjustment of Nature
|passage=She had seen fewer years than any of us, but she was of such superb Evehood and simplicity that she '''mothered''' us from the beginning.}}
# {{lb|en|transitive}} To cause to contain {{l|en|mother||that substance which develops in fermenting alcohol and turns it into vinegar}}.
#: {{ux|en|'''mothered''' oil'', '''''mothered''' vinegar'', '''''mothered''' wine}}
# {{lb|en|intransitive|of an alcohol}} To develop mother.
#* {{quote-book|en|year=1968|author=Evelyn Berckman|title=The Heir of Starvelings|page=172|passage=Iron rusted, paper cracked, cream soured and vinegar '''mothered'''.}}
#* {{quote-book|en|year=2013|author=Richard Dauenhauer|title=Benchmarks: New and Selected Poems 1963-2013|page=94|passage=Your lamp <br> was always polished, wick <br> trimmed, waiting; yet the bridegroom <br> somehow never came. Summer dust <br> settled in the vineyard. Grapes <br> were harvested; your parents <br> crushed and pressed them, but the wine <br> '''mothered'''.}}

=====Translations=====
{{trans-top|to treat as a mother would be expected to}}
* Danish: {{t+|da|mor|alt=være mor for}}, {{t|da|tage sig ordentlig af}}
* Dutch: {{t+|nl|bemoederen}}, {{t+|nl|koesteren}}
* Finnish: {{t|fi|[[olla]] [[äitinä]]}}
* French: {{t+|fr|materner}}
* German: {{t+|de|bemuttern}}
* Greek: {{t+|el|ανατρέφω}}, {{qualifier|informal}} {{t+|el|κανακεύω}}
* Hungarian: {{t|hu|[[anyáskodik]] (vki [[fölött]])}}
* Irish: {{t|ga|máithrigh}}
* Japanese: {{t-check|ja|母のように世話する|tr=[[はは]]のように[[せわ|せわする]], haha no yō ni sewa suru}}<!-- looks like a SOP. -->, {{t+check|ja|甘やかす|tr=[[あまやかす]], amayakasu}}
* Sinhalese: {{t|si|මාතෘ}}
* Swahili: {{t+|sw|mama}}
* Vietnamese: {{t+|vi|chăm sóc}}, {{t+|vi|nuôi}}, {{t+|vi|nuôi nấng}}
* Yiddish: {{t|yi|מאַמען}}
{{trans-bottom}}
"""
# myregl = myreg()
# getNoun = myregl.extractVerb(text)
#
# pprint.pprint(getNoun["Verb"])
