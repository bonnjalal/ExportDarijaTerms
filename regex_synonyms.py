import re
from regex_init import ReHelper
import pprint


reH = ReHelper()

lng = "en"


class myreg:

    def extractVerb(self, wikiText):
    
        itemFrom = self.getSynonyms(wikiText)

        return itemFrom
    
    def getSynonyms(self, text):
        items = {}

        synonymsPatt = r'(?<={{l\|'+lng+r'\|)(.*?)(?=}})'
        # uxPatt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
        # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'

        syMatchList = reH.reFindAll(synonymsPatt, text)

        items.update({"Synonyms":syMatchList})

        return items



txt = """
====Synonyms====
* {{l|en|adjectify}}
* {{l|en|adjectivize}}

"""

myregl = myreg()
getNoun = myregl.extractVerb(txt)

print(getNoun)
