from regex_adverb import AdvReg
from regex_etymology import EtyReg
from regex_adjective import AdjReg
from regex_noun import NounReg
from regex_pron import PronuncReg
from regex_pronoun import PronounReg
from regex_synonyms import SynReg
from regex_verb import VerbReg
from regex_altforms import AltReg


class ExtractHelper:
    def getSectContent(self, sectName, wikiTxt):

        sectNames = ["Etymology", "Pronunciation", "Verb", "Noun", "Adverb", "Adjective", "Pronoun", "Synonyms", "Alternative forms"]
        secDic = {}
        if sectName == sectNames[0]:
            myreg = EtyReg()
            secDic = myreg.extractFrom(wikiTxt)
        elif sectName == sectNames[1]:
            myreg = PronuncReg()
            secDic = myreg.extractPronunciation(wikiTxt)
        elif sectName == sectNames[2]:
            myreg = VerbReg()
            secDic = myreg.extractVerb(wikiTxt)
        elif sectName == sectNames[3]:
            myreg = NounReg()
            secDic = myreg.extractNoun(wikiTxt)
        elif sectName == sectNames[4]:
            myreg = AdvReg()
            secDic = myreg.extractVerb(wikiTxt)
        elif sectName == sectNames[5]:
            myreg = AdjReg()
            secDic = myreg.extractVerb(wikiTxt)
        elif sectName == sectNames[6]:
            myreg = PronounReg()
            secDic = myreg.extractVerb(wikiTxt)
        elif sectName == sectNames[7]:
            myreg = SynReg()
            secDic = myreg.extractVerb(wikiTxt)
        elif sectName == sectNames[8]:
            myreg = AltReg()
            secDic = myreg.extractAlt(wikiTxt)
        return secDic


