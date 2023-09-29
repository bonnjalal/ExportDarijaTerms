import re
from regex_init import ReHelper
# import pprint


reH = ReHelper()

lng = "ary"


class AdjReg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################
    


    def extractVerb(self, wikiText):
        # print(wikiText) 
        itemFrom = self.getAdjective(wikiText)

        return itemFrom

    #############################################
    
    # def getPlainLine(self, l):
    #     line = l
    #     # print(line) 
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
    #     line = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF\'(),;.\s]', '',line)
    #     # print("AFTER: "+line)
    #
    #     return line

   
    def getAdjItems(self, line):
        pattrs = {
            "Fem 1" : r'(?<=f\=)(.*?)(?=\|)',
            "Fem 2" : r'(?<=f2\=)(.*?)(?=\|)',
            "common pl 1" : r'(?<=cpl\=)(.*?)(?=\|)',
            "common pl 2" : r'(?<=cpl2\=)(.*?)(?=\|)',
            "mas pl 1" : r'(?<=pl\=)(.*?)(?=\|)',
            "mas pl 2" : r'(?<=pl2\=)(.*?)(?=\|)',
            "fem pl 1" : r'(?<=fpl\=)(.*?)(?=\|)',
            "fem pl 2" : r'(?<=fpl2\=)(.*?)(?=\|)' 
        }

        adjList = pattrs

        for key, value in pattrs.items():
            adjList[key] = reH.reFindFirst(value, line)

        return adjList


    def getAdjective(self, txt):
        sectionDic = {}
        items = {}

        adjItems = {}
        
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

            if "{{ary-adj" in l:
                adjItems = self.getAdjItems(l)
            elif l.startswith('# '):
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
        
        
        ### remove other meanings and keep only two
        # print(len(items))
        if len(items) == 0:
            sectionDic.update({1:{"meaning":'', "examples":[]}, 2:{"meaning":'', "examples":[]}})
        elif len(items) == 1:
            sectionDic.update({1:items[1], 2:{"meaning":'', "examples":[]}})
        else:
            sectionDic.update({1:items[1], 2:items[2]})
        # sectionDic.update(items)
        sectionDic.update(adjItems)
 
        # fromDic.update({"Etymology": items})
        
        return sectionDic

# text = ''
text = """
====Adjective====
{{en-adj|better|sup=best}}

# {{lb|en|of people}}
## Acting in the interest of what is [[beneficial]], [[ethical]], or [[moral]].
##: {{ux|en|'''good''' intentions}}
#* {{RQ:Wakefield Mystery Plays|play=Creation|page=6|lines=184–185|passage=It is not '''good''' to be alone, / to walk here in this worthely wone|t=It is not good to be alone, to walk here in this noble world}}
#** '''1500?''', [http://quod.lib.umich.edu/cgi/m/memem/memem-idx?fmt=entry&type=entry&byte=66789 Evil Tongues]ː
#**: If any man would begin his sins to reny, or any '''good''' people that frae vice deed rest ain. What so ever he were that to virtue would apply, But an ill tongue will all overthrow again.
#** {{RQ:Wilde Dorian Gray|6||When we are happy, we are always '''good''', but when we are '''good''', we are not always happy.}}
## [[competent|Competent]] or [[talent]]ed.
##: {{ux|en|a '''good''' swimmer}}
##* {{quote-book|en|year=1704|author=w:Robert South|title=Twelve Sermons Preached on Several Occasions|text=Flatter him it may, I confess, (as those are generally '''good''' at flattering who are '''good''' for nothing else,) but in the meantime the poor man is left under the fatal necessity of a needless delusion|section=On the nature and measure of conscience}}
##* {{quote-book|en|year=1922|author=w:Michael Arlen|title=[http://openlibrary.org/works/OL1519647W “Piracy”: A Romantic Chronicle of These Days]|chapter=3/19/2
|passage=Ivor had acquired more than a mile of fishing rights with the house ; he was not at all a '''good''' fisherman, but one must do something ; one generally, however, banged a ball with a squash-racket against a wall.}}
##* '''2016''', [https://web.archive.org/web/20170918070146/https://learningenglish.voanews.com/a/lets-learn-english-lesson-3-i-am-here/3126527.html VOA Learning English] (public domain)
##*: And Marsha says I am a '''good''' cook!
##*:: {{audio|en|And Marsha says I am a good cook!.ogg|Audio (US)}}
## Able to be depended on for the discharge of obligations incurred; of unimpaired credit; used with ''for''.
##: {{ux|en|Can you lend me fifty dollars? You know I'm '''good''' for it.}}
## [[well-behaved|Well-behaved]] (especially of children or animals).
##: {{ux|en|Be '''good''' while your mother and I are out.}}
##: {{ux|en|Were you a '''good''' boy for the babysitter?}}
## {{lb|en|US}} [[satisfied|Satisfied]] or [[at ease]]; not requiring more.
##: {{ux|en|Would you like a glass of water? &mdash; I'm '''good'''.}}
##: {{ux|en|[Are] you '''good'''? &mdash; Yeah, I'm fine.}}
##: {{ux|en|Gimme another beer! — I think you're '''good.'''}}
## {{lb|en|colloquial|with ''[[with]]''}} Accepting of, [[OK]] with
##: {{ux|en|My mother said she's '''good''' with me being alone with my date as long as she's met them first.}}
##: {{ux|en|The soup is rather spicy. Are you '''good''' with that, or would you like something else?}}
## {{lb|en|archaic}} Of high [[rank]] or [[birth]].
##* {{RQ:Shakespeare Richard 2|I|i|23|1–2|Thou art a Traitor, and a Miſcreant;<br>Too '''good''' to be ſo, and too bad to liue,<br>Since the more faire and chriſtall is the skie,<br>The vglier ſeeme the cloudes that in it flye:}}
# {{lb|en|of capabilities}}
## [[useful|Useful]] for a particular purpose; functional.
##: {{ux|en|it’s a '''good''' watch;&emsp; the flashlight batteries are still '''good'''}}
##* 1526, [http://quod.lib.umich.edu/cgi/m/memem/memem-idx?fmt=entry&type=entry&byte=326969 Herball]ː
##*: Against cough and scarceness of breath caused of cold take the drink that it hath been sodden in with Liquorice[,] or that the powder hath been sodden in with dry figs[,] for the same the electuary called dyacalamentum is '''good'''[,] and it is made thus.
##* {{quote-journal|en|year=2013|month=May-June|author=[http://www.americanscientist.org/authors/detail/david-van-tassel David Van Tassel]; [http://www.americanscientist.org/authors/detail/lee-dehaan Lee DeHaan]
|title=[http://www.americanscientist.org/issues/feature/2013/3/wild-plants-to-the-rescue Wild Plants to the Rescue]
|volume=101|issue=3|magazine=w:American Scientist
|passage=Plant breeding is always a numbers game.{{...}}The wild species we use are rich in genetic variation,{{nb...}}. In addition, we are looking for rare alleles, so the more plants we try, the better. These rarities may be new mutations, or they can be existing ones that are neutral—or are even selected against—in a wild population. A '''good''' example is mutations that disrupt seed dispersal, leaving the seeds on the heads long after they are ripe.}}
## [[effective|Effective]].
##: {{ux|en|a '''good''' worker}}
##* {{RQ:Belloc Lowndes Lodger|II|0091
|passage=There was a neat hat-and-umbrella stand, and the stranger's weary feet fell soft on a '''good''', serviceable dark-red drugget, which matched in colour the flock-paper on the walls.}}
## {{lb|en|obsolete}} Real; actual; serious.
##: {{ux|en|in '''good''' sooth}}
##* {{RQ:Shakespeare As You Like It|act=I|scene=ii|passage=Love no man in '''good''' earnest.}}
# {{lb|en|properties and qualities}}
## {{lb|en|of food}}
### Having a particularly [[pleasant]] taste.
###: {{ux|en|The food was very '''good'''.}}
###* '''c. 1430''' (reprinted '''1888'''), Thomas Austin, ed., ''Two Fifteenth-century Cookery-books. Harleian ms. 279 (ab. 1430), & Harl. ms. 4016 (ab. 1450), with Extracts from Ashmole ms. 1429, Laud ms. 553, & Douce ms. 55'' [Early English Text Society, Original Series; 91], London: [[w:Routledge|N. Trübner & Co.]] for the {{w|Early English Text Society}}, volume I, <small>[[w:Online Computer Library Center|OCLC]] [http://worldcat.org/oclc/374760 374760]</small>, page 11:
###*: Soupes dorye. — Take '''gode''' almaunde mylke {{...}} caste þher-to Safroun an Salt {{...}}
###* '''1962''' (quoting '''1381''' text), {{w|Hans Kurath}} & Sherman M. Kuhn, eds., ''{{w|Middle English Dictionary}}'', Ann Arbor, Mich.: {{w|University of Michigan Press}}, [[Special:BookSources/978-0-472-01044-8|ISBN 978-0-472-01044-8]], page 1242:
###*: '''dorrẹ̅''', '''dōrī''' adj. & n. {{...}} <u>cook</u>. glazed with a yellow substance; pome(s ~, sopes ~. {{...}} 1381 <u>Pegge Cook. Recipes</u> page 114: For to make Soupys dorry. Nym onyons {{...}} Nym wyn {{...}} toste wyte bred and do yt in dischis, and '''god''' Almande mylk.
### Being [[satisfying]]; meeting dietary requirements.
###: {{ux|en|Eat a '''good''' dinner so you will be ready for the big game tomorrow.}}
## Of food or other perishable products, still fit for use; not yet [[expired]], [[stale]], [[rotten]], etc.
##: {{ux|en|The bread is still '''good'''.}}
## [[valid|Valid]], of [[worth]], capable of being [[honour]]ed.
##: {{ux|en|This coupon is '''good''' for a free doughnut.}}
## [[true|True]], [[valid]], of [[explanatory]] strength.
##: {{ux|en|This theory still holds '''good''' even if much higher temperatures are assumed.}}
## [[healthful|Healthful]].
##: {{ux|en|Exercise and a varied diet are '''good''' for you.}}
## [[pleasant|Pleasant]]; [[enjoyable]].
##: {{ux|en|We had a '''good''' time.}}
## [[favourable|Favourable]].
##: {{ux|en|a '''good''' omen;&emsp; '''good''' weather}}
## Unblemished; honourable.
##: {{ux|en|a person's '''good''' name}}
## [[beneficial|Beneficial]]; [[worthwhile]].
##: {{ux|en|a '''good''' job}}
##* {{RQ:Maxwell Mirror and the Lamp|chapter=22|passage=Not unnaturally, “Auntie” took this communication in bad part.{{...}}Next day she{{...}}tried to recover her ward by the hair of the head. Then, thwarted, the wretched creature went to the police for help; she was versed in the law, and had perhaps spared no pains to keep on '''good''' terms with the local constabulary.}}
## Adequate; sufficient; not fallacious.
##* {{RQ:Shakespeare Taming of the Shrew|act=I|scene=i|passage=My reasons are both '''good''' and weighty.}}
##* {{quote-journal|en|year=1966|journal=Canadian Journal of Zoology|volume=44|issue=5|doi=10.1139/z66-095|author=K. Rothfels; Margaret Freeman|title=The salivary gland chromosomes of three North American species of ''Twinnia'' (Diptera: Simuliidae)|passage=''Twinnia biclavata'' differs from ''T. nova'' by inversion IS-1 and a nucleolar shift. Both are '''good''' species.}}
# {{lb|en|colloquial|when with ''[[and]]''}} [[very|Very]], [[extremely]]. See {{m|en|good and}}.
#: {{ux|en|The soup is '''good''' and hot.}}
# {{lb|en|colloquial}} [[ready|Ready]]
#: {{ux|en|I'm '''good''' when you are.}}
#: {{ux|en|The reports are [[good to go]].}}
# [[holy|Holy]] {{qualifier|especially when capitalized}} .
#: {{ux|en|[[Good Friday|'''Good''' Friday]], [[Good Wednesday|'''Good''' Wednesday]], the [[Good Book|'''Good''' Book]]}}
# {{lb|en|of quantities}}
## [[reasonable|Reasonable]] in amount.
##: {{ux|en|all in '''good''' time}}
## [[large|Large]] in amount or size.
##: {{ux|en|a '''good''' while longer;&emsp; {{nowrap|a '''good''' number of seeds;}}&emsp; {{nowrap|A '''good''' part of his day was spent shopping.}}&emsp; {{nowrap|It will be a '''good''' while longer until he's done.}}&emsp; {{nowrap|He's had a '''good''' amount of troubles, he has}}.}}
##* {{RQ:Marshall Squire's Daughter|III
|passage=The big houses, and there are a '''good''' many of them, lie for the most part in what may be called by courtesy the valleys. You catch a glimpse of them sometimes at a little distance from the [railway] line, which seems to have shown some ingenuity in avoiding them,{{nb...}}.}}
## [[full|Full]]; [[entire]]; [[at least]] as much as.
##: {{ux|en|This hill will take a '''good''' hour and a half to climb.&emsp; The car was a '''good''' ten miles away.}}
##* {{RQ:Besant Ivory Gate|chapter=Prologue|page=16|passage=Athelstan Arundel walked home all the way, foaming and raging. No omnibus, cab, or conveyance ever built could contain a young man in such a rage. His mother lived at Pembridge Square, which is four '''good''' measured miles from Lincoln's Inn.}}

=====Usage notes=====
The comparative {{m|en|gooder}} and superlative {{m|en|goodest}} are nonstandard.
In informal (often jocular) contexts, ''[[best]]'' may be inflected further and given the comparative ''[[bester]]'' and the superlative ''[[bestest]]''; these forms are also nonstandard.<!--if you update this usage note, also update the one in [[best]]-->

=====Synonyms=====
* {{sense|having positive attributes}} {{l|en|not bad}}, {{l|en|all right}}, {{l|en|satisfactory}}, {{l|en|decent}}, see also [[Thesaurus:good]]
* {{sense|healthful}} {{l|en|well}}
* {{sense|competent or talented}} {{l|en|accomplished}}
* {{sense|acting in the interest of good; ethical}} See [[Thesaurus:goodness]]

=====Antonyms=====
* {{sense|having positive attributes}} {{l|en|bad}}, {{l|en|poor}}
* {{sense|ethical}} {{l|en|bad}}, {{l|en|evil}}

=====Derived terms=====
{{der4|en|a good few|a good many|come from a good place|do well by doing good|dogoodery|double-plus-good|feelgoodery|fight the good fight|finger-lickin' good|for good|Good|good afternoon||good and|good as gold|good books|goodbye|good day|good drunk|gooden|good-for-nothing|good graces|good grief|goodish|good job|good morning|goodly|good money|good-neighbourly|goodness|good night|good riddance|good riddance to bad rubbish|Good Samaritan|good sense|goodsome|good to go
|good works|hold good|talk a good game|the good die young|today is a good day to die|too much of a good thing|ungood|you can't keep a good man down|good show|'sall good|a bad tree does not yield good apples|a change is as good as a rest|a good beginning makes a good ending|a good deal|a good deed is its own reward|a good look|a miss is as good as a mile|a nod is as good as a wink|a nod's as good as a wink to a blind bat|all good|all good in the hood|all good things come to an end|all good things must come to an end|all in good time|all publicity is good publicity|all-good|anti-good|any press is good press|as good as|as good as it gets|as good as new|bad money drives out good|baked good|be good for|better is the enemy of good|club good|come good|common good|complementary good|consumer good|demerit good|digital good|do good|do more harm than good|do someone's heart good|double-plus-good|durable good|enough is as good as a feast|every good boy deserves fudge|fake good|fat lot of good|feel-good|feel-good factor|finished good|for good and all|for good measure|for good or ill|for one's own good|for the love of all that is good|from good hands|get out while the getting's good|Giffen good|give a good account of oneself|give as good as one gets|go gentle into that good night|good and proper|good as new|good as one's word|good as wheat in the bin|good bet|good bishop|good black don't crack|good boi|good book|good breath|good bye|good cess|good cop bad cop|good delivery|good doctor|good egg|good ending|good enough|good enough for government work|good enough for jazz|good enough to eat|good evening|good faith|good fences make good neighbors|good fences make good neighbours|good folk|good for a laugh|good for nothing|good for someone|good form|good fortune|Good Friday|good game|good God|good Goddess|good going|good golly|good gracious|good gravy|good guy|good head on one's shoulders|good heav'ns|good heavens|good house|good humor|good humour|goodie|good lack|good language|good law|good leg|good length|good lick|good life|good liking|good looker|good looking|good looks|good Lord|good luck|goodman|good manners|good morrow|good name|good nature|good news|good night's sleep|good now|good offices|good oil|good ol'|good ol' boy|good old|good old boy|good old boy network|good old days|good ole|good ole boy|good on someone|good one|good people|good press|good question|good shit|good sort|good speed|good spirits|good sport|good standing|good thing|good things come in small packages|good things come in threes|good things come to those who wait|good thinking|good time|good time Charley|good time Charlie|good time girl|good times|good trouble|good try|good turn|good value|good voice to beg bacon|good will|good willer|good wine needs no bush|good word|good work|good-bad|good-brother|good-by|good-bye|good-byer|good-den|good-fellowship|good-good|good-hearted|good-heartedly|good-heartedness|good-humored|good-humoredly|good-humoredness|good-humoured|good-humouredly|good-humouredness|good-king-henry|good-looking|good-lookingness|good-minded|good-natured|good-naturedly|good-naturedness|good-neighborliness|good-neighbourliness|good-sized|good-tempered|good-temperedness|good-time|good-time Charley|good-time Charlie|good-time girl|good-timer|goodwife|goody|grave good|grave-good|greater good|have a good one|have a good time|have something on good authority|hunger is a good sauce|I'm good|in good conscience|in good hands|in good odor|in good odour|in good part|in good spirits|in good stead|in good time|inferior good|it's all good|it's an ill wind that blows no good|it's an ill wind that blows no one any good|it's an ill wind that blows nobody any good|Joan's as good as my lady in the dark|job's a good 'un|jolly good show|keep good hours|let the door hit you where the good Lord split you|let the good times roll|let the perfect be the enemy of the good|luxury good|make a good fist of|make good|make good on|make good time|make the perfect the enemy of the good|merit good|no good|no good deed ever goes unpunished|no good deed goes unpunished|no news is good news|no-good|no-good ass|nobody ever went broke underestimating the good taste of the American people|nobody ever went broke underestimating the good taste of the American public|normal good|on a good wicket|on good terms|on someone's good side|one good turn deserves another|only the good die young|pass a good time|perfect is the enemy of good|perfect is the enemy of good enough|perfection is the enemy of good|positional good|private good|producer good|producer's good|public good|put in a good word|put to good use|quite good|romping good|scrape-good|seem like a good idea at the time|so far so good|something good|stand in good stead|stroy-good|stry-good|substitute good|superior good|that's a good one|the best defense is a good offense|the best is the enemy of the good|the better is the enemy of the good|the fox may grow grey but never good|the good doctor|the great and the good|the perfect is the enemy of the good|the road to hell is paved with good intentions|there's many a good tune played on an old fiddle|throw good money after bad|to the good|too good for this world|too good to be true|too good to last|turn to good account|twelve good men and true|uber-good|up to no good|Veblen good|very good|walk good|waste good|waste-good|well and good|what good is|what's good|what's good for the goose is good for the gander|what's the good of|will the good of another|with good grace|with good reason|you have to be good to be lucky|you're good|you're only as good as your last shift|your good name|your good self|your guess is as good as mine}}

=====Translations=====
{{trans-top|acting in the interest of good; ethical good intentions}}
{{multitrans|data=
* Adyghe: {{t|ady|шӏу}}
* Afrikaans: {{tt+|af|goed}}
* Albanian: {{tt+|sq|mirë}}
* Alviri-Vidari: {{qualifier|Vidari}} {{tt|avd|ودر|tr=vader}}
* Ambonese Malay: {{tt|abs|bai}}, {{tt|abs|ae}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Amharic: {{tt|am|ጥሩ}}
* Arabic: {{tt+|ar|حَسَن}}, {{tt|ar|جَيِّد}}, {{tt|ar|طَيِّب}}
*: Egyptian Arabic: {{tt|arz|كويس|tr=kwayyes}}
*: Moroccan Arabic: {{tt|ary|مزِيان|tr=mazyan}}, {{tt|ary|ملِيح|tr=mliḥ}}
*: North Levantine Arabic: {{tt|apc|منيح|tr=mnīḥ}}
*: South Levantine Arabic: {{tt|ajp|طَيِّب|tr=tayyeb}}, {{tt|ajp|كويس|tr=kwayyes}}, {{tt|ajp|منيح|tr=mnīḥ}}
*: Tunisian Arabic: {{tt|aeb|باهي|tr=bāhi}}
* Aramaic: {{tt|arc|טבא|sc=Hebr}}
* Argobba: {{t|agj|ጥሩ|tr=ṭeru}}
* Armenian: {{tt+|hy|լավ}}, {{tt+|hy|բարի}}
* Aromanian: {{tt|rup|bun|m}}, {{tt|rup|bunã|f}}
* Assamese: {{tt|as|ভাল}}
* Asturian: {{tt+|ast|bonu}}
* Azerbaijani: {{tt+|az|yaxşı}}, {{tt+|az|xeyir}}, {{tt+|az|xoş}}
* Bashkir: {{tt|ba|яҡшы|sc=Cyrl}}
* Belarusian: {{tt+|be|до́бры}}
* Bengali: {{tt+|bn|ভাল}}, {{t+|bn|নেক}}
* Bikol Central: {{tt+|bcl|marhay}}
* Bulgarian: {{tt+|bg|добъ́р}}
* Burmese: {{tt+|my|ကောင်း|sc=Mymr}}
* Buryat: {{t|bua|һайн}}
* Catalan: {{tt+|ca|bo}}, {{tt+|ca|bon}}
* Cebuano: {{tt|ceb|maayo}}, {{t|ceb|maayohon}}
* Chamicuro: {{tt|ccc|pewa}}
* Chechen: {{t|ce|дика}}
* Chickasaw: {{tt|cic|chokma}}
* Chinese:
*: Dungan: {{tt|dng|хо}}
*: Mandarin: {{tt+|cmn|好|tr=hǎo}}, {{tt+|cmn|良|tr=liáng}}
*: Min Dong: {{tt|cdo|好|tr=ho}}
* Coptic: {{tt|cop|ⲁⲅⲁⲑⲟⲥ}} {{qualifier|Sahidic, Bohairic}}
* Czech: {{tt+|cs|dobrý}}
* Dalmatian: {{tt|dlm|bun|m}}, {{tt|dlm|buna|f}}
* Danish: {{tt+|da|god|m}}, {{tt+|da|godt|n}}
* Dutch: {{tt+|nl|goed}}
* Eastern Bontoc: {{tt|ebk|ammay}}
* Egyptian: {{t-egy|mꜣꜥ|h=mA-mAa:a:Y1}}
* Erromintxela: {{t|emx|latxo}}
* Esperanto: {{tt+|eo|bona}}
* Estonian: {{tt+|et|hea}}
* Evenki: {{t|evn|ая}}
* Faliscan: {{tt|xfa|dueno}}
* Faroese: {{tt+|fo|góður}}
* Finnish: {{tt+|fi|hyvä}}
* Franco-Provençal: {{tt|frp|bon}}
* French: {{tt+|fr|bon|m}}, {{tt+|fr|bonne|f}}
* Friulian: {{tt|fur|bon}}
* Galician: {{tt|gl|boo|m}}, {{tt|gl|boa|f}}
* Georgian: {{tt+|ka|კარგი}}
* German: {{tt+|de|gut}}
* Gothic: {{tt|got|𐌲𐍉𐌸𐍃}}, {{tt|got|𐌸𐌹𐌿𐌸𐌴𐌹𐌲𐍃}}
* Greek: {{tt+|el|καλός}}, {{tt+|el|αγαθός}}
*: Ancient: {{tt|grc|ἀγαθός}}, {{tt|grc|ἐσθλός}} {{qualifier|Epic}}
* Gujarati: {{tt|gu|સારું}}
* Haitian Creole: {{tt|ht|bon}}
* Hebrew: {{tt+|he|טוֹב|tr=tov}}
* Higaonon: {{t|mba|maayad}}
* Hiligaynon: {{t|hil|maayo}}
* Hindi: {{tt+|hi|अच्छा}}, {{tt+|hi|भला}}, {{tt+|hi|उत्तम}}, {{tt+|hi|नेक}}, {{tt+|hi|खूब}}, {{tt|hi|ख़ूब}}, {{tt+|hi|नीति}}
* Hiri Motu: {{t|ho|namo}}
* Hittite: {{t|hit|𒀀𒀸𒋗𒍑 |tr=a-aš-šu-uš}}
* Hungarian: {{tt+|hu|jó}}
* Icelandic: {{tt+|is|góður|m}}, {{tt|is|góð|f}}, {{tt|is|gott|n}}
* Ido: {{tt+|io|benigna}}, {{tt+|io|bona}}
* Ilocano: {{tt|ilo|naimbag}}
* Indonesian: {{tt+|id|baik}}
* Ingrian: {{tt|izh|hyvä}}
* Ingush: {{t|inh|дика}}
* Iranun: {{t|ill|mapia}}
* Irish: {{tt+|ga|maith}}
* Istro-Romanian: {{tt|ruo|bur}}
* Italian: {{tt+|it|buono}}
* Japanese: {{tt+|ja|良い|tr=よい, yoi}}, {{tt+|ja|いい|tr=ii}}, {{tt+|ja|善意|alt=善意の|tr=ぜんいの, zen'i no}}
* Kabardian: {{t+|kbd|фӏы}}
* Kalmyk: {{t|xal|сән}}
* Kannada: {{tt+|kn|ಉತ್ತಮ|sc=Knda}}
* Kashubian: {{t|csb|dobri}}
* Kazakh: {{tt+|kk|жақсы|sc=Cyrl}}
* Khmer: {{tt+|km|ល្អ}}
* Khün: {{t-needed|kkh}}
* Kikuyu: {{tt|ki|-ega}}
* Korean: {{tt+|ko|좋다}}
* Kumyk: {{tt|kum|яхшы|tr=yaxşı}}
* Kurdish:
*: Northern Kurdish: {{t+|kmr|baş}}
* Kyrgyz: {{tt+|ky|жакшы|sc=Cyrl}}
* Ladin: {{tt|lld|bon}}
* Lao: {{tt+|lo|ດີ}}
* Latgalian: {{tt|ltg|lobs|m}}
* Latin: {{tt+|la|bonus}}
* Latvian: {{tt+|lv|labs|m}}
* Lithuanian: {{tt+|lt|geras}}
* Livonian: {{tt|liv|jõvā}}
* Lombard: {{t|lmo|bón}}
* Lü: {{tt|khb|ᦡᦲ}}
* Luxembourgish: {{tt|lb|gutt}}
* Macedonian: {{tt|mk|добар|sc=Cyrl}}
* Maguindanao: {{t|mdh|mapia}}
* Malay: {{tt+|ms|baik}}
* Malayalam: {{tt+|ml|നല്ലത്|sc=Mlym}}
* Maltese: {{tt+|mt|tajjeb}}
* Manchu: {{t|mnc|ᠰᠠᡳᠨ}}
* Manggarai: {{t|mqy|di'a}}
* Maori: {{tt+|mi|pai}}
* Maranao: {{t|mrw|mapia}}
* Marathi: {{tt|mr|चांगला|sc=Deva}}, {{tt|mr|चांगली|sc=Deva}}, {{tt|mr|चांगले|sc=Deva}}, {{tt|mr|भला|sc=Deva}}, {{tt|mr|भली|sc=Deva}}, {{tt|mr|भले|sc=Deva}}
* Mauritian Creole: {{t|mfe|bon}}
* Mazanderani: {{tt|mzn|خار|tr=xar|sc=mzn-Arab}}
* Mbyá Guaraní: {{t|gun|ha'eve}}, {{t|gun|porã}}
* Middle Persian: {{tt|pal|𐭭𐭩𐭪|ts=nēk|sc=Phli}}
* Mòcheno: {{tt|mhn|guat}}
* Mongolian: {{tt+|mn|сайн|sc=Cyrl}}
* Motu: {{t|meu|namo}}
* Nanai: {{t|gld|улэн}}
* Navajo: {{tt|nv|yáʼátʼééh}}
* North Frisian: {{tt|frr|gödj}}
* Northern Kankanay: {{tt|xnn|gawis}}
* Northern Thai: {{tt|nod|ᨯᩦ|tr=di|sc=Lana}}
* Norwegian: {{tt+|no|god}}, {{tt+|no|godt}}
* Occitan: {{tt+|oc|bon}}
* Old Church Slavonic: {{tt|cu|добръ|sc=Cyrs}}
* Old Frisian: {{tt|ofs|gōd}}
* Old Javanese: {{t|kaw|bĕcik}}
* Old Norse: {{tt|non|góðr}}
* Old Turkic: {{tt|otk|𐰓𐰏𐰇|tr=edgü}}
* Ossetian: {{tt|os|хорз}}
* Papiamentu: {{t|pap|bon}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Persian: {{tt+|fa|خوب|tr=xub}}, {{tt+|fa|نیک|tr=nik}}
* Pijin: {{t|pis|gudfala}}
* Plautdietsch: {{tt+|pdt|goot}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom}}
* Punjabi: {{tt|pa|ਚੰਗਾ}}
* Quechua: {{tt|qu|allin}}
* Romagnol: {{t|rgn|bôn}}
* Romani: {{t|rom|laćho}}
* Romanian: {{tt+|ro|bun|m}}, {{tt+|ro|bună|f}}
* Romansch: {{tt|rm|bun}}
* Russian: {{tt+|ru|хоро́ший}}, {{tt+|ru|до́брый}}
* Sanskrit: {{tt+|sa|साधु}}, {{tt|sa|सु-}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian:
*: Cyrillic: {{tt|sh|до̏бар|sc=Cyrl}}
*: Roman: {{tt+|sh|dȍbar}}
* Shan: {{tt+|shn|လီ}}
* Sicilian: {{tt+|scn|bonu}}
* Sinhalese: {{tt+|si|හොඳ|sc=Sinh}}
* Slovak: {{tt+|sk|dobrý}}
* Slovene: {{tt+|sl|dóber}}
* Somali: {{t|so|wanaagsan}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry}}
* Southern Kalinga: {{tt|ksc|mamfaru}}
* Spanish: {{tt+|es|bueno}}
* Sundanese: {{tt|su|hadé}}
* Swahili: {{tt+|sw|nzuri}}, {{t|sw|njema}}
* Swedish: {{tt+|sv|god|c}}, {{tt+|sv|gott|n}}, {{t+|sv|bra}}
* Sylheti: {{tt|syl|ꠜꠣꠟꠣ}}
* Tagalog: {{tt|tl|mabuti}}, {{tt|tl|mabait}}
* Tai Dam: {{t-needed|blt}}
* Tajik: {{tt+|tg|хуб|sc=Cyrl}}
* Talysh: {{qualifier|Asalemi}} {{tt|tly|چاک|tr=câk|sc=fa-Arab}}
* Tamil: {{tt+|ta|நன்மை|sc=Taml}}
* Tarantino: {{t|roa-tar|bbuène}}
* Tatar: {{tt+|tt|яхшы|sc=Cyrl}}
* Telugu: {{tt+|te|మంచి}}, {{tt+|te|నీతి}}
* Tetum: {{t|tet|di'ak}}
* Thai: {{tt+|th|ดี}}, {{tt|th|ดี ๆ|tr=dii dii}}
* Tibetan: {{t|bo|བཟང}}
* Tillamook: {{t|til|də húcsənə}}
* Tok Pisin: {{tt|tpi|gutpela}}
* Turkish: {{tt+|tr|iyi}}
* Turkmen: {{tt+|tk|gowy}}, {{tt|tk|ýagşy}}
* Tzotzil: {{tt|tzo|lek}}
* Ugaritic: {{tt|uga|𐎉𐎁}}
* Ukrainian: {{tt+|uk|до́брий}}, {{tt|uk|хоро́ший}}, {{tt+|uk|га́рний}}
* Urdu: {{tt|ur|اچھا|m|tr=acchā}}, {{tt|ur|بهلا|m|tr=bhalā}}
* Uyghur: {{tt+|ug|ياخشى|sc=ug-Arab}}
* Uzbek: {{tt+|uz|yaxshi}}
* Venetian: {{tt+|vec|bon}}
* Vietnamese: {{tt+|vi|tốt}}, {{tt+|vi|hay}}, {{tt+|vi|tuyệt}}
* Vilamovian: {{tt|wym|güt}}
* Votic: {{tt|vot|üvä}}
* Walloon: {{tt+|wa|bon}}
* Waray-Waray: {{tt|war|maupay}}
* Welsh: {{tt+|cy|da}}
* West Frisian: {{tt|fy|goed}}
* Western Bukidnon Manobo: {{t|mbb|me'upiya}}
* White Hmong: {{tt|mww|zoo}}
* Yagnobi: {{tt|yai|хуб}}
* Yakut: {{tt|sah|үчүгэй|sc=Cyrl}}
* Yiddish: {{tt|yi|גוט}}
* Zazaki: {{tt+|zza|weş}}
* Zealandic: {{tt|zea|goed}}
* Zhuang: {{tt|za|ndei}}
{{trans-bottom}}

{{trans-top|well-behaved}}
* Chickasaw: {{tt|cic|chokma}}
* French: {{tt+|fr|sage}}
* German: {{t+|de|brav}}, {{t+|de|gehörig}}
* Turkish: {{t+|tr|terbiyeli}}, {{t+|tr|efendi}}
{{trans-bottom}}

{{trans-top|useful for a particular purpose}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Arabic: {{tt+|ar|حَسَن}}, {{tt|ar|جَيِّد}}
* Armenian: {{tt+|hy|լավ}}
* Aromanian: {{tt|rup|bun}}
* Bulgarian: {{tt+|bg|добъ́р}}, {{tt+|bg|доброка́чествен}}
* Catalan: {{tt+|ca|bo}}
* Chamicuro: {{tt|ccc|pewa}}
* Cherokee: {{t|chr|ᎣᏍᏓ}}
* Chinese:
*: Mandarin: {{tt+|cmn|好|tr=hǎo}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god|m}}, {{tt+|da|godt|n}}
* Dutch: {{tt+|nl|goed}}
* Extremaduran: {{tt|ext|güenu}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* Friulian: {{tt|fur|bon}}
* Galician: {{tt+|gl|bo|m}}
* Georgian: {{tt+|ka|კარგი}}
* German: {{tt+|de|gut}}
* Gothic: {{tt|got|𐌲𐍉𐌸𐍃}}, {{tt|got|𐌸𐌹𐌿𐌸𐌴𐌹𐌲𐍃}}
* Greek: {{tt+|el|καλός}}
*: Ancient: {{tt|grc|ἀγαθός}}, {{tt|grc|ἐσθλός}} {{qualifier|Epic}}
* Haitian Creole: {{tt|ht|bon}}
* Hebrew: {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}
* Ido: {{tt+|io|bona}}
* Indonesian: {{tt+|id|bagus}}
* Irish: {{tt+|ga|maith}}
* Istro-Romanian: {{tt|ruo|bbur}}
* Italian: {{tt+|it|buono|m}}
* Japanese: {{tt+|ja|良い|tr=[[よい]], yoi}}, {{tt+|ja|いい|tr=ii}}
* Khmer: {{tt|km|គ្រប់គ្រាន់|tr=krup kroan|sc=Khmr}}
* Korean: {{tt+|ko|좋은}}
* Latvian: {{tt+|lv|labs|m}}
* Luxembourgish: {{tt|lb|gutt}}
* Middle Korean: {{t|okm|됴타|tr=tyǒhón|alt=됴〯ᄒᆞᆫ〮}}
* Navajo: {{tt|nv|yáʼátʼééh}}
* Ngazidja Comorian: {{tt|zdj|ema|alt=-ema}}
* Northern Sami: {{tt|se|buorrẹ}}
* Norwegian: {{tt+|no|god}}, {{tt+|no|godt}}
* Ojibwe: {{t|oj|mino-}}
* Old Church Slavonic: {{tt|cu|добръ|sc=Cyrs}}
* Ossetian: {{tt|os|хорз}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Persian: {{tt+|fa|خوب|tr=xub}}
* Pite Sami: {{tt|sje|buorre}}
* Plautdietsch: {{tt+|pdt|goot}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom}}
* Quechua: {{tt|qu|alli}}, {{tt|qu|allin}}
* Rapa Nui: {{tt|rap|riva}}
* Romanian: {{tt+|ro|bun}}
* Russian: {{tt+|ru|хоро́ший}}, {{tt+|ru|неплохо́й}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian:
*: Cyrillic: {{tt|sh|до̏бар|sc=Cyrl}}
*: Roman: {{tt+|sh|dȍbar}}
* Sinhalese: {{tt+|si|හොඳ|sc=Sinh}}
* Skolt Sami: {{tt|sms|šiõǥǥ}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}
* Sylheti: {{t|syl|ꠜꠣꠟꠣ}}
* Tamil: {{t+|ta|நல்ல}}
* Telugu: {{tt+|te|మంచిది}}
* Thai: {{qualifier|informal}} {{tt|th|ดูดี|tr=doo dee}}, {{qualifier|formal}} {{tt|th|สวยงาม|tr=sŭay ngaam}}
* Tocharian B: {{tt|txb|kartse}}
* Tok Pisin: {{tt|tpi|gutpela}}
* Tongan: {{tt|to|lelei}}
* Tuvaluan: {{tt|tvl|lelei}}, {{tt|tvl|llei}}
* Ukrainian: {{tt+|uk|добрий}}, {{tt|uk|хороший}}
* Venetian: {{tt+|vec|bon}}
* Vietnamese: {{tt+|vi|tốt}}
* Vilamovian: {{tt|wym|güt}}
* Welsh: {{tt+|cy|da}}
* Yakut: {{tt|sah|үчүгэй|sc=Cyrl}}
{{trans-bottom}}

{{trans-top|of food, edible; not stale or rotten}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Bengali: {{tt+|bn|তাজা}}
* Bulgarian: {{tt+|bg|добъ́р}}, {{tt+|bg|го́ден}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god|m}}, {{tt+|da|godt|n}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* Galician: {{tt+|gl|bo|m}}
* Georgian: {{tt+|ka|კარგი}}
* German: {{tt+|de|gut}}
* Hebrew: {{tt+|he|אכיל}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt|hi|ताज़ा}}, {{tt+|hi|ताजा}}
* Ido: {{tt+|io|bona}}, {{tt+|io|manjebla}}
* Italian: {{tt+|it|buono}}, {{tt+|it|mangiabile}}
* Japanese: {{t+check|ja|大丈夫|alt=大丈夫な|tr=[[だいじょうぶ]]な, daijōbuna}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}
* Luxembourgish: {{tt|lb|gutt}}
* Norwegian: {{tt+|no|god}}, {{tt+|no|godt}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Plautdietsch: {{tt+|pdt|goot}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|dobro}}, {{tt+|sh|valjano}}, {{tt+|sh|dobar|m}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
* Spanish: {{tt+|es|bueno}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}
* Telugu: {{tt+|te|తాజా}}
* Welsh: {{tt+|cy|blasus}}
{{trans-bottom}}

{{trans-top|of food, having a particularly pleasant taste}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Breton: {{tt+|br|mat}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{tt+|cmn|好吃|tr=hǎochī}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god|m}}, {{tt+|da|godt|n}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* German: {{tt+|de|lecker}}, {{tt+|de|gut}}
* Hebrew: {{tt|he|טעים|tr=ta'ím}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|पसंद}}
* Ido: {{tt+|io|bona}}, {{tt+|io|saporoza}}
* Italian: {{tt+|it|buono|m}}
* Japanese: {{t+|ja|美味しい|tr=oishii}}, {{t+|ja|美味い|tr=umai}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt|lv|gards|m}}
* Luxembourgish: {{tt|lb|gutt}}
* Norwegian: {{tt+|no|god}}, {{tt+|no|godt}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom}}
* Quechua: {{tt+|qu|sumaq}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|ukusno}}, {{tt+|sh|dobro}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|god|c}}, {{tt+|sv|gott|n}}
* Telugu: {{tt+|te|పసందు}}
* Ukrainian: {{t+|uk|до́брий}}
* Vietnamese: {{t+|vi|ngon}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|healthful}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Bengali: {{tt|bn|স্বাস্থ্যকর|sc=Beng}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|sund}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}, {{tt+|fi|terveellinen}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}, {{tt+|de|gesund}}
* Hebrew: {{tt+|he|בריא|tr=barí}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}
* Ido: {{tt+|io|bona}}, {{tt+|io|salubra}}
* Italian: {{tt+|it|salutare}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}, {{tt|lv|vērtīgs|m}}, {{tt|lv|veselīgs|m}}
* Luxembourgish: {{tt|lb|gutt}}, {{tt|lb|gesond}}
* Mazanderani: {{tt|mzn|خار|tr=xar|sc=mzn-Arab}}
* Norwegian: {{tt+|no|sunn}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|dobro}}, {{tt+|sh|zdravo}}, {{tt+|sh|zdrav}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}, {{tt+|sv|nyttig}}
* Telugu: {{tt+|te|ఆరోగ్యకరమైన}}
* Welsh: {{tt+|cy|iachus}}
{{trans-bottom}}

{{trans-top|pleasant; enjoyable}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Bulgarian: {{tt+|bg|ху́бав}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god}}, {{tt|da|fin}}
* Dutch: {{tt+|nl|goed}}
* Egyptian: {{t-egy|nfr|h=nfr-f:r}}
* Esperanto: {{tt+|eo|bona}}
* Finnish: {{tt+|fi|mukava}}, {{tt+|fi|hauska}}, {{tt+|fi|kiva}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}, {{tt+|de|schön}}, {{tt+|de|angenehm}}
* Gothic: {{tt|got|𐌲𐍉𐌸𐍃}}
* Greek: {{tt+|el|καλός}}
* Hebrew: {{tt|he|מהנה|tr=mehané}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}
* Ido: {{tt+|io|bona}}, {{tt+|io|benigna}}, {{tt+|io|agreabla}}
* Italian: {{tt+|it|buono|m}}
* Japanese: {{tt+|ja|良い|tr=よい, yoi|sc=Jpan}}, {{tt+|ja|いい|tr=ii|sc=Jpan}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}, {{tt|lv|patīkams|m}}
* Lithuanian: {{tt+|lt|geras|m}}
* Mòcheno: {{tt|mhn|guat}}
* Navajo: {{tt|nv|yáʼátʼééh}}
* Norwegian: {{tt+|no|god}}
* Ojibwe: {{t|oj|mino-}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom|m}}, {{tt+|pt|boa|f}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|godno}}, {{tt+|sh|ugodno}}, {{tt+|sh|čedno}}, {{tt+|sh|dobro}}
* Slovene: {{tt+|sl|dóber}}
* Somali: {{t|so|wacan}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Sundanese: {{tt+|su|saé}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}
* Telugu: {{tt|te|ఉత్సోహకరము}}
* Tibetan: {{tt|bo|ཡག་པོ}}
* Turkish: {{tt+|tr|iyi}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|of people, competent or talented}}
* Armenian: {{tt+|hy|լավ}}
* Bulgarian: {{tt+|bg|добъ́р}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{tt+|cmn|嫻熟|tr=xiánshú}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god}}, {{tt+|da|dygtig}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}
* Hebrew: {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}
* Ido: {{tt+|io|bona}}, {{tt+|io|kompetenta}}
* Italian: {{tt+|it|bravo}}
* Japanese: {{tt+|ja|良い|tr=よい, yoi}}, {{tt+|ja|いい|tr=ii|sc=Jpan}}, {{tt+|ja|上手|tr=じょうずな, jōzu-na|alt=上手な|sc=Jpan}}, {{tt+|ja|旨い|tr=うまい, umai|sc=Jpan}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}
* Norwegian: {{tt+|no|god}}, {{tt+|no|flink}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom|m}}, {{tt+|pt|boa|f}}
* Russian: {{tt+|ru|хоро́ший}}, {{tt+|ru|уме́лый}}, {{tt+|ru|иску́сный}}, {{qualifier|agile}} {{tt+|ru|ло́вкий}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|spretan|m}}, {{tt|sh|spretna|f}}, {{tt+|sh|blagotvorna|f}}, {{tt+|sh|blagotvoran|m}}, {{tt+|sh|sposoban|m}}, {{tt|sh|sposobna|f}}, {{tt+|sh|dobar}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Sundanese: {{tt|su|hadé}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}
* Tagalog: {{tt|tl|magaling}}
* Telugu: {{tt|te|చురుకుతనము}}
* Vietnamese: {{tt+|vi|giỏi}}, {{tt+|vi|khá}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|effective}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Bengali: {{tt|bn|কার্যকর|sc=Beng}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}, {{tt+|de|effektiv}}
* Hebrew: {{tt+|he|יעיל}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt|hi|शक्तिवंत}}, {{tt+|hi|कर्माकारी}}
* Ido: {{tt+|io|bona}}, {{tt+|io|efektiva}}, {{tt|io|efektema}}
* Italian: {{tt+|it|ottimo}}, {{tt+|it|bravo}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}, {{tt|lv|efektīvs|m}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom|m}}, {{tt+|pt|boa|f}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|dobro}}, {{tt+|sh|dobar}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}, {{tt+|sv|god}}
* Tagalog: {{tt|tl|may bisa}}, {{tt|tl|magaling}}
* Telugu: {{tt+|te|శక్తివంతము}}
* Tok Pisin: {{tt|tpi|gutpela}}
* Vietnamese: {{tt+|vi|khá}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|favourable}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}, {{tt+|hy|բարի}}
* Bulgarian: {{tt+|bg|добъ́р}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}
* Hebrew: {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}, {{tt+|hi|अभिमान}}
* Ido: {{tt+|io|bona}}
* Italian: {{tt+|it|favorevole}}
* Japanese: {{tt+|ja|良い|tr=よい, yoi}}, {{tt+|ja|いい|tr=ii|sc=Jpan}}
* Korean: {{t-needed|ko}}
* Latin: {{tt+|la|bonus}}
* Latvian: {{tt+|lv|labs|m}}, {{tt+|lv|labvēlīgs|m}}
* Mòcheno: {{tt|mhn|guat}}
* Navajo: {{tt|nv|yáʼátʼééh}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom|m}}, {{tt+|pt|boa|f}}, {{tt+|pt|boa|f}}
* Russian: {{tt+|ru|хоро́ший}}, {{tt+|ru|до́брый}} {{q|of an omen}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|pouzdano}}, {{tt+|sh|dobar}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Sundanese: {{tt+|su|saé}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}, {{tt+|sv|god|c}}, {{tt+|sv|gott|n}}
* Telugu: {{tt+|te|అభిమానము}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|beneficial; worthwhile}}
* American Sign Language: {{tt|ase|OpenB@Chin-PalmBack-OpenB@CenterChesthigh-PalmUp OpenB@Palm-PalmUp-OpenB@CenterChesthigh-PalmUp}}
* Armenian: {{tt+|hy|լավ}}
* Bengali: {{tt|bn|উপকারি|sc=Beng}}
* Catalan: {{tt+|ca|bo}}
* Chinese:
*: Mandarin: {{t-needed|cmn}}
* Czech: {{tt+|cs|dobrý}}
* Danish: {{tt+|da|god}}
* Dutch: {{tt+|nl|goed}}
* Finnish: {{tt+|fi|hyvä}}
* French: {{tt+|fr|bon|m}}
* Galician: {{tt+|gl|bo|m}}
* German: {{tt+|de|gut}}
* Hebrew: {{tt+|he|מוצלח|tr=mutzlákh}}, {{tt+|he|טוב|tr=tóv}}
* Hindi: {{tt+|hi|उत्तम|m}}, {{tt+|hi|अच्छा|m}}, {{tt|hi|अच्छी|f}}, {{tt|hi|अच्छे|p}}, {{tt+|hi|उपकारी}}, {{tt|hi|उपयोगकार}}
* Ido: {{tt+|io|bona}}
* Italian: {{tt+|it|buon}}
* Korean: {{t-needed|ko}}
* Latvian: {{tt+|lv|labs|m}}, {{tt|lv|vērtīgs|m}}
* Pashto: {{tt+|ps|ښه|tr=ẍë}}
* Polish: {{tt+|pl|dobry}}
* Portuguese: {{tt+|pt|bom|m}}, {{tt+|pt|boa|f}}
* Russian: {{tt+|ru|хоро́ший}}
* Scots: {{tt|sco|guid}}
* Scottish Gaelic: {{tt|gd|math}}
* Serbo-Croatian: {{tt+|sh|pouzdana}}, {{tt+|sh|korisna}}, {{tt+|sh|dobar}}
* Slovene: {{tt+|sl|dóber}}
* Sorbian:
*: Lower Sorbian: {{tt|dsb|dobry}}
*: Upper Sorbian: {{tt+|hsb|dobry|m}}
* Spanish: {{tt+|es|bueno}}
* Swahili: {{tt+|sw|mzuri}}
* Swedish: {{tt+|sv|bra}}, {{tt+|sv|god}}
* Telugu: {{tt+|te|ఉపయోగకరము}}
* Welsh: {{tt+|cy|da}}
{{trans-bottom}}

{{trans-top|full; entire; at least}}
* Hungarian: {{tt+|hu|jó}}, {{t+|hu|bő}}
* Polish: {{t+|pl|dobry}}
* Swedish: {{t+|sv|dryg}}
}}
<!-- close {{multitrans}} -->
{{trans-bottom}}

{{checktrans-top}}
* Afrikaans: {{t+check|af|goed}}
* Albanian: {{t+check|sq|mirë}}
* Arabic: {{t-check|ar|جَيِّد}}, {{t-check|ar|طَيِّب}}, {{t+check|ar|حَسَن}}
* Avar: {{t-check|av|лъикӏаб}}
* Azerbaijani: {{t+check|az|yaxşı}}
* Bengali: {{t+check|bn|ভাল}}
* Cebuano: {{t-check|ceb|maayo}}
* Esperanto: {{t+check|eo|bona}}
* Fijian: {{t-check|fj|vinaka}}
* Guaraní: {{t+check|gn|porã}}
* Hittite: {{t-check|hit|aššu|sc=Xsux}}
* Indonesian: {{t+check|id|baik}}, {{t+check|id|bagus}}
* Interlingua: {{t-check|ia|bon}}
* Inuktitut: {{t-check|iu|pitsiartok|sc=Cans}}
* Italian: {{t+check|it|buono}}
* Korean: {{t+check|ko|좋은|sc=Kore}}
* Kurdish:
*: Northern Kurdish: {{t+check|kmr|baş}}, {{t+check|kmr|qenc}}, {{t+check|kmr|çê}}, {{t+check|kmr|çak}}, {{t+check|kmr|rind}}
* Lakota: {{t-check|lkt|washte}}
* Lithuanian: {{t+check|lt|geras}}
* Ojibwe: {{t-check|oj|mino-|sc=Cans}}
* Persian: {{t+check|fa|خوب|tr=xub}}
* Romani: {{t-check|rom|laćho}}
* Romanian: {{t+check|ro|bun}}
* Serbo-Croatian: {{t-check|sh|добро}}, {{t+check|sh|dobro}}
* Sicilian: {{t+check|scn|bonu}}
* Slovak: {{t+check|sk|dobrý}}
* Swahili: {{t-check|sw|-zuri}}
* Tamil: {{t+check|ta|நன்று|sc=Taml}}
* Telugu: {{t+check|te|మంచి}}(maMci)
* Thai: {{t+check|th|ดี|tr=dee|sc=Thai}}
* Tupinambá: {{t-check|tpn|katu}}
* Turkish: {{t+check|tr|yakşı}}
* Urdu: {{t-check|ur|اچھا|m|sc=ur-Arab}}, {{t-check|ur|اچھی|f|sc=ur-Arab}}, {{t-check|ur|اجھے|p|sc=ur-Arab}}
* Uzbek: {{qualifier|yaxşi}} {{t-check|uz|яхши}}
* Walloon: {{t+check|wa|bon}}
* Yiddish: {{t-check|yi|גוט}}
{{trans-bottom}}

"""
myregl = AdjReg()
getNoun = myregl.extractVerb(text)

print(getNoun)
