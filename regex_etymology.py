import re
from regex_init import ReHelper


reH = ReHelper()

lng = "en"


class myreg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################
    


    def extractFrom(self, wikiText):
    
        itemFrom = self.getFrom(wikiText)

        return itemFrom

    #############################################

    
    def getFrom(self, txt):
        types = ["inh", "bor", "der"]
        fromDic = {}
        items = {}

        i = 1
        for t in types:
        
            pattern = r'{{'+t+r'\|'+lng+r'\|(.*?)}}'
            # lngPattern = r'(?<=.'+t+r'\|)(.*?)(?=}})'
 
            matchList = reH.finditer_with_line_numbers(pattern, txt)
            if len(matchList) > 0:
                for i in range(len(matchList)):
                    # print(matchList[i][0])
                    lngPattern = r'(?<={{'+t+r'\|'+lng+r'\|)(.*?)(?=\|)'
                    fromLng = reH.reFindFirst(lngPattern, matchList[i][0])

                    wordPattern = r'(?<={{'+t+r'\|'+lng+r'\|'+fromLng+r'\|)(.*?)(?=\|)'
                    wordPatternBak = r'(?<={{'+t+r'\|'+lng+r'\|'+fromLng+r'\|)(.*?)(?=}})'

                    translationPatt = r'(?<=\|t=)(.*?)(?=\|)' 
                    transliterationPatt = r'(?<=\|tr=)(.*?)(?=\|)'
 
                    fromWord = reH.reFindFirst(wordPattern, matchList[i][0], wordPatternBak)
                    
                    translationPattBak = r'(?<=\|t=)(.*?)(?=}})'
                    transliterationPattBak = r'(?<=\|tr=)(.*?)(?=}})' 

                    translation = reH.reFindFirst(translationPatt, matchList[i][0], translationPattBak) 
                    
                    transliteration = reH.reFindFirst(transliterationPatt, matchList[i][0],transliterationPattBak)

                    item = {t + " From "+ str(i): {fromLng: fromWord, "translation": translation, "transliteration": transliteration}}
                    items.update(item)
                    i +=1
        fromDic.update({"Etymology": items})

        return fromDic





text = '''===Etymology===
    [[File:Zakat al-fitr. Makhachkala. 2016.jpg|thumb|[[wheat#Noun|Wheat]] collected as zakat for [[charitable]] [[distribution]] at the [[w:Grand Mosque of Makhachkala|Grand Mosque]] of [[Makhachkala]] in [[Dagestan]], [[Russia]].]]

    Borrowed from:

    * {{bor|en|fa|زکات|tr=zakât}};
    * {{bor|en|tr|zekât}}, from {{der|en|ota|زكات|tr=zekat}}; or
    * {{bor|en|ur|زکات|tr=zakāt}};<ref>{{R:Lexico|pos=n}}</ref>

    all from {{der|en|ar|زَكَاة|t=almsgiving, zakat; purification}},<ref>{{R:OED Online|pos=n|id=5113619279|date=April 2023}}</ref> from {{m|ar|زَكَوٰة|tr=zakāh}} {{qualifier|archaic}}, from {{der|en|arc|זכותא}}/{{m|syc|ܙܟܘܬܐ|tr=zākūṯā|t=goodness, probity, uprightness; merit; victory}}, from {{m|arc|זכי|tr=zəḵē|t=to gain; to overcome, triumph over}}.
    From {{inh|en|enm|storm|t=disturbed state of the atmosphere; heavy precipitation; battle, conflict; attack}}{{nb...|starme, steorm, storem, storme, stourme, strom|otherforms=1}},<ref>{{R:MED Online|pos=n|id=MED43115}}</ref> from {{der|en|ang|storm|t=tempest, storm; attack; storm of arrows; disquiet, disturbance, tumult, uproar; onrush, rush}}{{nb...|steorm, (Northern England) stearm|otherforms=1}}, from {{inh|en|gmw-pro|*sturm|t=storm}}, from {{der|en|gem-pro|*sturmaz|t=storm}}, from {{der|en|ine-pro|*(s)twerH-|t=to agitate, stir up; to propel; to urge on}}.<ref name="OED">Compare {{R:OED Online|pos=n|date=July 2023|nodot=1}}; {{R:Lexico|pos=n}}</ref> Related to {{m|en|stir}}.
    '''

myregl = myreg()
getFrom = myregl.extractFrom(text)

print(getFrom)
