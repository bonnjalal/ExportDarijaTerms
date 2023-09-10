import re
from regex_init import ReHelper
import pprint


reH = ReHelper()

lng = "en"


class myreg:
  # def __init__(self):
    # self.name = name
    # self.age = age

    #Check if the string starts with "The" and ends with "Spain":
   
    ##### Etymology ##################
    


    def extractNoun(self, wikiText):
    
        itemFrom = self.getNoun(wikiText)

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
 
    def getNoun(self, txt):
        nounDic = {}
        items = {}
        
        # text = '''_YES_ '''

        lines = txt.splitlines()

        # isline = False
        i = 0

        meaning = ""
        examplesList = []

        for l in lines:
            if l.startswith('# '):
                if i>0 :
                    items.update({i:{"meaning": meaning, "examples":examplesList}})

                line = self.getPlainLine(l)
                meaning = line
                i+=1
                # text += "\n" + line
            elif  l.startswith('#:'):
                line = self.getPlainLine(l)
                examplesList.append(line)
                # text += "\n" + line

        nounDic.update({"Noun": items})
 
        # fromDic.update({"Etymology": items})
        
        return nounDic






text = r"""
====Noun====
{{en-noun}}

# A [[female]] [[parent]], sometimes' especially a [[human]]; a female who [[parent#Verb|parent]]s a [[child]] (which she has given birth to, adopted, or fostered).
#: {{ux|en|I am visiting my '''mother''' today.}}
#: {{ux|en|The lioness was a '''mother''' of four cubs.}}
# A [[female]] who has given [[birth]] to a [[baby]]; this person in relation to her child or children.
#: {{ux|en|My sister-in-law has just become a '''mother''' for the first time.}}
#: {{ux|en|He had something of his '''mother''' in him.}}
#* {{quote-book|en|year=1988|author=Robert Ferro|title=Second Son|passage=He had something of his '''mother''' in him, but this was because he realized that in the end only her love was unconditional, and in gratitude he had emulated her.}}
#* {{quote-book|en|year=2005|author=Trudelle Thomas|title=Spirituality in the Mother Zone: Staying Centered, Finding God|publisher=Paulist Press|isbn=9780809142989|page=41
|text=The "Ritual to Celebrate Birthing" begins with a leader welcoming all participants : "Welcome to this celebration for ''N''. She is approaching the time when she will become a '''mother''' for the first time (or become a '''mother''' again).}}
# A [[pregnant]] female, possibly as a shortened form of [[mother-to-be]]; a female who [[gestate]]s a baby.
#: {{ux|en|Nutrients and oxygen obtained by the '''mother''' are conveyed to the fetus.}}
#* {{quote-text|en|year=1991|author=w:Susan Faludi|title=The Undeclared War Against American Women
|passage=The antiabortion iconography in the last decade featured the fetus but never the '''mother'''.}}
#* {{quote-book|en|title=Multiplicity Yours: Cloning, Stem Cell Research, and Regenerative Medicine|isbn=9789814477567
|text=To clone a boy, it is necessary to have a man as a DNA donor, a woman as an egg donor, and may be another woman as a surrogate '''mother'''.}}
#* {{quote-book|en|date=2023-01-16|author=Reinhard Renneberg|title=Biotechnology for Beginners|publisher=Academic Press|isbn=9780323855709|page=317
|text=If the cat to be cloned is female, the nucleus donor cat could also be used as the surrogate '''mother''' instead of another cat.}}
# A female who [[donate]]s a [[fertilize]]d [[egg]] or donates a body cell which has resulted in a [[clone]].
# {{lb|en|figuratively}} A female [[ancestor]].
#* {{RQ:Tyndale Pentateuch|Genesis|3|20|v|And Adã called his wyfe Heua&nbsp;/ becauſe ſhe was the '''mother''' of all that lyveth}}
# {{lb|en|figuratively}} A source or origin.
#: {{ux|en|The Mediterranean was '''mother''' to many cultures and languages.}}
#* {{RQ:Shakespeare Macbeth|IV|iii|147|1|Alas poore Countrey, / Almoſt affraid to know it ſelfe. It cannot / Be call’d our '''Mother''', but our Graue;}}
#* {{quote-book|en|year=1844|author=w:Thomas Arnold|title=Fragment on the Church|volume=1|pageurl=http://books.google.com.au/books?id=hh8UAAAAQAAJ&pg=PA17&dq=%22mother+falsehood+from+which+all+idolatry+is+derived%22&hl=en&sa=X&ei=p09OU4rYBYGbkgWItICgCg&redir_esc=y#v=onepage&q=%22mother%20falsehood%20from%20which%20all%20idolatry%20is%20derived%22&f=false|page=17
|passage=But one in the place of God and not God, is as it were a falsehood; it is the '''mother''' falsehood from which all idolatry is derived.}}
#* {{quote-journal|en|author=Rowena Mason|quotee=w:David Steel|title=Lord Steel criticises culture of spin and tweeting in modern politics|work=The Guardian|date=2013-10-31|url=https://www.theguardian.com/politics/2013/oct/31/lord-steel-criticises-culture-spin-doctors-twitter-politics|issn=0261-3077|passage=How on earth are we supposed to hold our heads high as the ‘'''mother''' of parliaments’ when we allow to continue the practice of almost openly buying a seat in parliament?}}
# Something that is the [[greatest]] or most [[significant]] of its [[kind]]. {{q|See {{m|en|mother of all}}.}}
#* '''1991''', January 17, {{w|Saddam Hussein}}, Broadcast on Baghdad state radio.
#*: The great duel, the '''mother''' of all battles has begun.
# {{lb|en|dated|when followed by a surname}} A title of respect for one's mother-in-law.
#: {{ux|en|'''Mother''' Smith, meet my cousin, Doug Jones.}}
# {{lb|en|dated}} {{n-g|A term of address for one's [[wife]].}}
#* {{quote-journal|en|date=2 April 1887|author=E. V. Wilson|title=Uncle Dave|journal=The Current|volume=7|number=172|page=432|pageurl=https://books.google.co.uk/books?id=RavPAAAAMAAJ&pg=PA432|text=A few minutes later we were all seated comfortably, Uncle Dave and '''mother''', as he called his wife, myself and my husband, in the split-bottomed wooden chairs, on the vine-covered porch. / “Is Bethel a Methodist Church?” I asked. / Uncle Dave looked quizzically at his wife. “Do you hear that, '''mother'''?” he said.}}
#* {{quote-book|en|year=1922|author=w:Stephen Leacock|title=Sunshine Sketches of a Little Town|url=https://books.google.co.uk/books?id=HxNIAAAAMAAJ|page=152|text=On some days as he got near the house he would call out to his wife: / “Almighty Moses, Martha! who left the sprinkler on the grass?” / On other days he would call to her from quite a little distance off: “Hullo, '''mother'''! Got any supper for a hungry man?”}}
#* {{quote-book|en|year=1944|author={{w|Walter C. Hackett|Walter Hackett}}|title=For the Duration: A Play for Junior and Senior High Schools|page=8|pageurl=https://books.google.co.uk/books?id=UPkhgxwthfsC&pg=PA8|text=({{small caps|Mr. Hill}} ''enters. He crosses to'' {{small caps|Wife}}.) / {{small caps|Mr. Hill:}} Hello, '''mother'''. {{...}} How are you? / {{small caps|Mrs. Hill:}} Nothing wrong, dear, I hope.}}
# {{lb|en|figuratively}} Any [[elderly]] [[woman]], especially within a particular [[community]].
# {{lb|en|figuratively}} Any person or entity which performs [[mothering]].
#* [[Judges]] [http://bible.cc/judges/5-7.htm 5:7], [[KJV]].
#*: The inhabitants of the villages ceased, they ceased in Israel, until that I Deborah arose, that I arose a '''mother''' in Israel.
#* [[Galatians]] [http://bible.cc/galatians/4-26.htm 4:26], KJV.
#*: Jerusalem which is above is free, which is the '''mother''' of us all.
# [[dregs|Dregs]], [[lees]]; a [[stringy]], [[mucilaginous]] or [[film]]- or [[membrane]]-like substance {{gloss|consisting of [[acetobacter]]s}} which develops in fermenting alcoholic liquids {{gloss|such as wine, or cider}}, and turns the alcohol into [[acetic acid]] with the help of [[oxygen]] from the [[air]].
#: {{ux|en|pieces of '''mother''''', ''adding '''mother''' to vinegar}}
# {{lb|en|railroading}} A [[locomotive]] which provides [[electrical]] [[power]] for a [[slug]].
# The principal piece of an [[astrolabe]], into which the others are fixed.
# The female [[superior]] or head of a religious house; an [[abbess]], etc.
# {{lb|en|obsolete}} Hysterical passion; [[hysteria]]; the [[uterus]].
#* {{RQ:Shakespeare King Lear Q1|II|iv|page=47|passage=O how this '''mother''' ſwels vp toward my hart{{...}}}}
#* {{quote-text|en|year=1665|author=Robert Lovel|title=Pambotanologia sive Enchiridion botanicum|page=484
|passage=T.V. dicusseth tumors and mollifieth them, helps inflammations, rising of the '''mother''' and the epilepsie being burnt.}}
#* {{quote-text|en|year=1666|author=Nicholas Culpeper|title=The English Physitian Enlarged|page=49
|passage=The Root hereof taken with Zedoary and Angelică, or without them,  helps the rising of the '''Mother'''.}}
#* {{quote-book|en|year=1979|author=Thomas R. Forbes|chapter=The changing face of death in London|editor=Charles Webster|title=Health, Medicine and Mortality in the Sixteenth Century|year_published=1979|page=128
|passage=St Botolph's parish records ascribed three deaths to &apos;'''mother'''&apos;, an old name for the uterus.}}
# A [[disc]] produced from the [[electrotype]]d [[master]], used in manufacturing [[phonograph record]]s.

=====Synonyms=====
* {{sense|one’s female parent}} See also [[Thesaurus:mother]]
* {{sense|most significant thing}} {{l|en|father}}, {{l|en|grandfather}}, {{l|en|granddaddy}}
* {{sense|of or pertaining to the mother, such as [[metropolis]]}} {{l|en|metro-}}

=====Antonyms=====
* {{qualifier|with regards to gender}} [[father]]
* {{qualifier|with regards to ancestry}} [[daughter]], [[son]], [[child]], [[offspring]]

=====Hypernyms=====
* {{sense|a female parent}} {{l|en|parent}}

=====Coordinate terms=====
* {{sense|a female parent}} {{l|en|father}}

=====Derived terms=====
{{col4|en
|antimother
|be mother
|biological mother
|birth mother
|foster mother
|founding mother
|godmother
|grandmother
|great-grandmother
|motherboard
|Mother City
|mother country
|Mother Earth
|mother figure
|motherfucker
|Mothering Sunday
|mother-in-law
|motherland
|motherless
|motherlike
|motherline
|motherload
|mother lode
|motherly
|mother of all
|mother ship
|Mother's Day
|mother-to-be
|mother tongue
|mother wit
|motherwort
|mothery
|refrigerator mother
|stepmother
|surrogate mother
| adoptive mother|and his mother|baby mother|bonus mother|brother from another mother|bunny mother|camp mother|co-mother|co-mother-in-law|corn mother|cow-mother|den mother|do you kiss your mother with that mouth|earth mother|everybody and his mother|everybody and their mother|everyone and his mother|everyone and their mother|face only a mother could love|face that only a mother could love|fuck your mother|gold star mother|like a mother hawk|megaspore mother cell|milk mother|milk-mother|mother abscess|mother bomb|mother church|mother dough|mother fucker|mother goddess|mother hen|mother heroine|mother hive|mother language|mother liquor|mother may I|mother naked|mother of chapel|mother of coal|mother of pearl|mother of thousands|mother plant|mother sauce|mother sauces|mother superior|mother-bird|mother-fucker|mother-hen|mother-hive|mother-in-law apartment|mother-in-law sandwich|mother-in-law seat|mother-in-law style|mother-in-law's tongue|mother-lode|mother-naked|mother-of-pearl|mother-of-thyme|mother-out-law|mother-spot|mother-tongue|mother-wit|my very educated mother just served us nachos|my very educated mother just served us nine pumpkins|my very educated mother just served us noodles|necessity is the mother of innovation|necessity is the mother of invention|queen mother|she could be his mother|she's the cat's mother|single mother|stage mother|step-mother|sweet Mary mother of God|sweet mother of God|sweet mother of Jesus|sweet mother of pearl|tiger mother|welfare mother|wolf-mother|you kiss your mother with that mouth|your mother}}

=====Related terms=====
{{col4|en|title=Etymologically related
|matter
|material
|maternal
|maternity
|matriculate
|matrimony
|matrix
}}
{{prefixsee|en|matri-}}

=====Descendants=====
* {{desc|ja|マザー|tr=mazā|bor=1}}
* {{desc|ko|마더|bor=1}}
* {{desc|rop|motha}}

=====Translations=====
{{see translation subpage|Noun}}

"""
myregl = myreg()
getNoun = myregl.extractNoun(text)

pprint.pprint(getNoun)
