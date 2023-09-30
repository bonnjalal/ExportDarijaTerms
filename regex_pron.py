import re

from regex_init import ReHelper

reH = ReHelper()
lng = "ary"
class PronuncReg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################

  def extractPronunciation(self, wikiText):
    ####### Pronunciation ###########

    #lines = txt.splitlines()
    
    pron = self.getPron(wikiText)

    audios = self.getAudio(wikiText)
    # rhymesDic = self.getRhymes(wikiText)

    pronDict = {}
    pronDict.update(pron)
    pronDict.update(audios)
    # pronDict.update(rhymesDic)

    pronunciationDic = pronDict

    # print(pronunciationDic)

    return pronunciationDic

    #############################################

  def getRhymes(self, txt):
    rhymesPattern = r'(?<={{rhymes\|'+lng+r'\|)(.*?)(?=\|)'
    rhymes = reH.reFindFirst(rhymesPattern, txt)
    rhymesDic = {"rhymes":""}
    if len(rhymes) >=0 :
      rhymesDic.update({"rhymes": rhymes})
    return rhymesDic


  def getPron(self, txt):
    # i = 0
    
    pronPattern = r'(?<={{ary-IPA\|)(.*?)(?=}})'
    pronBkpPattr = r'(?<={{IPA\|'+lng+r'\|)(.*?)(?=}})'
    accentPattern = r'{{a\|(.*?)}}'
    # pattern = '{{IPA\|en\|(.*?)}}' 
    # accent = re.findall(r'{{a\|(.*?)}}', txt) 
    # pron = re.findall(r'{{IPA\|en\|(.*?)}}', txt)
    matchList = reH.finditer_with_line_numbers(pronPattern, txt)
    if len(matchList) <=0:
      matchList = reH.finditer_with_line_numbers(pronBkpPattr, txt) 
    
    if len(matchList) <=0:
      return {}

    pronDic = {}
    items = {}
    for i in range(len(matchList)):
       if len(pronDic) >= 2:
         break
       accent = reH.reFindFirst(accentPattern, matchList[i][2], default=lng)
       item = {"accent":accent, "text":matchList[i][0]}
       # items.update(item)

       pronDic.update({"pron_text " + str(i+1):item})
        

    return pronDic

  def getAudio(self, txt):
    types = ["ogg", "mp3", "wav", "flac", "mid"]
    audiosDic = {"Audios":[]}
    # items = {}
    items = []
    for t in types:
        # if len(items) >=2:
                  # break

        audioPattern = r'(?<='+lng+r'\|)(.*?)(?=.'+t+r'\|)'
        lngPattern = r'(?<=.'+t+r'\|)(.*?)(?=}})'
 
        matchList = reH.finditer_with_line_numbers(audioPattern, txt)
        # print(matchList)
        if len(matchList) > 0:
            for i in range(len(matchList)):
                # if len(items) >=2:
                  # break
                # audioLng = re.findall(lngPattern, matchList[i][2])
                # item = {audioLng[0]: matchList[i][0] + '.' + t}
                # item = {len(items)+1: matchList[i][0] + '.' + t}
                item = matchList[i][0] + '.' + t
                items.append(item)

                # print("audio" + str(item))
                # items.update(item)

    # print(items)
    audiosDic.update({"Audios":items})


    return audiosDic
 
  def getAudio2(self, txt):
    types = ["mp3", "ogg", "wav", "flac", "mid"]
    audiosDic = {}
    i = 0
    items = {}
    for t in types:
      audio = re.findall(r'en\|(.*?).'+t+r'\|', txt)
      audio_lang = re.findall(r'.'+t+r'\|(.*?)}}', txt)

      #audioDic = {"audio_list":audio, "audio_lang_list": audio_lang}
      if len(audio) >= 0:

        for a in range(len(audio)):
          item = {audio_lang[a]: audio[a]+'.'+t}
          items.update(item)
          # item = {"audio": audio[a]+'.'+t, "audio_lang": audio_lang[a]}
          # audiosDic.update({"item {}".format(i): item})
          i+=1
          #newAudio.append(a+'.'+t)
        audiosDic.update(items)
        # print(audiosDic)
        #audios += newAudio
    return audiosDic
   



text = '''* {{a|RP}} {{IPA|en|/stɔːm/}}
  * {{a|GA}} {{IPA|en|/stɔɹm/}}a
  * {{a|Gn}} {{IPA|en|/stɔɹm/}}a
  * {{audio|en|En-us-storm.ogg|Audio (GA)}}
  * {{rhymes|en|ɔː(ɹ)m|s=1}}
  * {{audio|en|En-us-storm.wav|Audio (US)}}
  * {{audio|en|En-us-storm.mp3|Audio (US)}}
  '''

# myreg = PronuncReg()
# result = myreg.extractPronunciation(text)
# print(result)
