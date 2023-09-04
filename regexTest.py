import re


lng = "en"
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
    
    pron = self.getPron(wikiText)
    # pron = re.findall(r'{{IPA\|'+lng+'\|(.*?)}}', txt)
    ##audio = re.findall(r'en\|(.*?).ogg\|', txt)
    rhymes = re.findall(r'{{rhymes\|'+lng+'\|(.*?)\|', wikiText)

    #print(rhymes)
    audios = self.getAudio(wikiText)
    print(pron)

    #############################################
  def getPron(self, txt):
    pronDic = {}
    i = 0
    items = {}
    
    pattern = '(?<={{IPA\|en\|)(.*?)(?=}})'
    # pattern = '{{IPA\|en\|(.*?)}}' 
    # accent = re.findall(r'{{a\|(.*?)}}', txt) 
    # pron = re.findall(r'{{IPA\|en\|(.*?)}}', txt)
    matchList = finditer_with_line_numbers(pattern, txt)
    print(matchList)

  
  def getAudio(self, txt):
    types = ["mp3", "ogg", "wav", "flac", "mid"]
    audiosDic = {}
    i = 0
    items = {}
    for t in types:
      audio = re.findall(r'en\|(.*?).'+t+'\|', txt)
      audio_lang = re.findall(r'.'+t+'\|(.*?)}}', txt)

      #audioDic = {"audio_list":audio, "audio_lang_list": audio_lang}
      if len(audio) >= 0:

        for a in range(len(audio)):
          item = {audio_lang[a]: audio[a]+'.'+t}
          items.update(item)
          # item = {"audio": audio[a]+'.'+t, "audio_lang": audio_lang[a]}
          # audiosDic.update({"item {}".format(i): item})
          i+=1
          #newAudio.append(a+'.'+t)
        audiosDic.update({"Audio": items})
        # print(audiosDic)
        #audios += newAudio
    return audiosDic
   
def finditer_with_line_numbers(pattern, string, flags=0):
    '''
    A version of 're.finditer' that returns '(match, line_number)' pairs.
    '''
    import re

    matches = list(re.finditer(pattern, string, flags))
    if not matches:
        return []

    end = matches[-1].start()
    # -1 so a failed 'rfind' maps to the first line.
    newline_table = {-1: 0}
    for i, m in enumerate(re.finditer('\\n', string), 1):
        # Don't find newlines past our last match.
        offset = m.start()
        if offset > end:
            break
        newline_table[offset] = i

    # Failing to find the newline is OK, -1 maps to 0.

    matcheslist = {}

    for m in matches:
        newline_offset = string.rfind('\n', 0, m.start())
        newline_end = string.find('\n', m.end())  # '-1' gracefully uses the end.
        line = string[newline_offset + 1:newline_end]
        line_number = newline_table[newline_offset]
        mList = [m.group(), line_number, line]
        matcheslist.update({m.group():mList})

    return matcheslist


text = '''* {{a|RP}} {{IPA|en|/stɔːm/}}
  * {{a|GA}} {{IPA|en|/stɔɹm/}}a
  * {{audio|en|En-us-storm.ogg|Audio (GA)}}
  * {{rhymes|en|ɔː(ɹ)m|s=1}}
  * {{audio|en|En-us-storm.wav|Audio (US)}}'''

myregl = myreg()
myregl.extractPronunciation(text)
