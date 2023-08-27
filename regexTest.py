import re

class myreg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################

  def extractPronunciation(self, wikiText):
    ####### Pronunciation ###########

    #lines = txt.splitlines()
    #pron_lang = re.findall(r'{{IPA\|(.*?)\|', txt)
    #print(pron_lang)

    #pron = re.findall(r'{{IPA\|en\|(.*?)}}', txt)
    ##audio = re.findall(r'en\|(.*?).ogg\|', txt)
    #rhymes = re.findall(r'{{rhymes\|en\|(.*?)\|', txt)

    #print(rhymes)
    audios = self.getAudio(txt)
    print(audios)

    #############################################

  def getAudio(self, txt):
    types = ["mp3", "ogg", "wav", "flac", "mid"]
    audiosDic = {}
    i = 0
    for t in types:
      audio = re.findall(r'en\|(.*?).'+t+'\|', txt)
      audio_lang = re.findall(r'.'+t+'\|(.*?)}}', txt)

      #audioDic = {"audio_list":audio, "audio_lang_list": audio_lang}
      
      if len(audio) >= 0:
        #newAudio = {}
        for a in range(len(audio)):
          item = {"audio": audio[a]+'.'+t, "audio_lang": audio_lang[a]}
          audiosDic.update({"item {}".format(i): item})
          i+=1
          #newAudio.append(a+'.'+t)
        #audios += newAudio

    return audiosDic
   

txt = '''* {{a|RP}} {{IPA|en|/stɔːm/}}
  * {{a|GA}} {{IPA|en|/stɔɹm/}}a
  * {{audio|en|En-us-storm.ogg|Audio (GA)}}
  * {{rhymes|en|ɔː(ɹ)m|s=1}}
  * {{audio|en|En-us-storm.wav|Audio (US)}}'''

myreg = myreg()
myreg.extractPronunciation(txt)
