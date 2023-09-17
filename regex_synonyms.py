import re
from regex_init import ReHelper
# import pprint


reH = ReHelper()

lng = "ary"


class SynReg:

    def extractVerb(self, wikiText):
    
        itemFrom = self.getSynonyms(wikiText)

        return itemFrom
    
    def getSynonyms(self, text):
        items = {}
        
        lines = text.splitlines()


        lPatt = r'(?<={{l\|'+lng+r'\|)(.*?)(?=}})'
        syn2Patt = r'(?<=\|)(.*?)(?=|)'
 
        syMatchList = []
        for l in lines:
            if r"{{l|" in l:
                syMatchList += reH.reFindAll(lPatt, l)
            elif r"{{syn|" in l:
                sysList = reH.reFindAll(syn2Patt, l)

                newSynList = []
                for syn in sysList:
                    line = re.sub(r'[\u0621-\u064A]', '',syn)
                    if (line != ''):
                        newSynList.append(line)

                syMatchList += newSynList

                        



        # synPatt = r'(?<={{syn\|'+lng+r'\|)(.*?)(?=}})'
         
 #        synBkpPatt = r'(?<={{syn\|'+lng+r'\|)(.*?)(?=|)'
 #        syn2Patt = r'(?<=\|)(.*?)(?=|tr)'
 # 

        # uxPatt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
        # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'

       
        # syMatchList = reH.reFindAll(synPatt, text, synBkpPatt)

        items.update(syMatchList)

        return items



txt = """
====Synonyms====
* {{l|en|adjectify}}
* {{l|en|adjectivize}}

"""

# myregl = myreg()
# getNoun = myregl.extractVerb(txt)
#
# print(getNoun)
