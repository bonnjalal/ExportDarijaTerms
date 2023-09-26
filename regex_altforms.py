import re

from regex_init import ReHelper

lng = "ary"

reH = ReHelper()
class AltReg:
    def extractAlt(self, wikiText):
    
        altDic = self.getAlt(wikiText) 

        return altDic

    def getAlt(self, text):
        # items = {}
        
        lines = text.splitlines()


        # altPatt = r'(?<={{alter\|'+lng+r'\|)(.*?)(?=}})'
        # synBkpPatt = r'(?<=\|)(.*?)(?=\|)'
        # syn2Patt = r'(?<={{syn\|)(.*?)(?=\<)'
 
        syMatchList = []
        for l in lines:
            if "{{alter|" in l:
                line = re.sub(r'[^\u0600-\u06FF\|]', '',l)
                # line = line.replace('|', ' ')

                # line = line.strip()
                # print(line)
                sList = list(line.split("|"))
                for s in sList:
                    alt = s.strip()
                    if alt != "" and alt != " " and alt != "   " and alt != "    ":
                        alt = alt.replace('|', '') 
                        syMatchList.append(alt)
                # print(syMatchList)

                        
        return syMatchList

# altR = AltReg()
#
# text = """
# * {{alter|ary|نجاص|tr1=ngāṣ|لنجاص|tr2=langāṣ}}
# """
#
# print(altR.getAlt(text))
