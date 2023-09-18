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
        # items = {}
        
        lines = text.splitlines()


        lPatt = r'(?<={{l\|'+lng+r'\|)(.*?)(?=}})'
        # synBkpPatt = r'(?<=\|)(.*?)(?=\|)'
        # syn2Patt = r'(?<={{syn\|)(.*?)(?=\<)'
 
        syMatchList = []
        for l in lines:
            if r"{{l|" in l:
                syMatchList += reH.reFindAll(lPatt, l)
            elif "{{syn|" in l:
                line = re.sub(r'[^\u0600-\u06FF\|]', '',l)
                line = line.replace('|', ' ')

                line = line.strip()
                # print(line)
                sList = list(line.split(" "))
                for s in sList:
                    if s != "" and s != " " and s != "  " and s != "   " and s != "    ":
                        syMatchList.append(s)
                # print(syMatchList)

                        



        # synPatt = r'(?<={{syn\|'+lng+r'\|)(.*?)(?=}})'
         
 #        synBkpPatt = r'(?<={{syn\|'+lng+r'\|)(.*?)(?=|)'
 #        syn2Patt = r'(?<=\|)(.*?)(?=|tr)'
 # 

        # uxPatt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
        # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'

       
        # syMatchList = reH.reFindAll(synPatt, text, synBkpPatt)

        # items.update(syMatchList)
        

        return syMatchList



# txt = """
# #: {{syn|ary|ضر|tr1=ḍarr|جرح|tr2=jraḥ}}"""
#
# myregl = SynReg()
# getNoun = myregl.getSynonyms(txt)
#
# print(getNoun)
