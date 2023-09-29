import re


lng = "ary"
class ReHelper:
    
    def reFindFirst(self, pattern, string, bakPattern=None, default=''):
        try:
            return re.findall(pattern, string)[0]
        except :
            if bakPattern != None:
                try:
                    return re.findall(bakPattern, string)[0] 
                except :
                    return default
            else:
                return default

    def reFindAll(self, pattern, string, bakPattern=None, default=[]):
        try:
            return re.findall(pattern, string)
        except :
            if bakPattern != None:
                try:
                    return re.findall(bakPattern, string)    
                except :
                    return default
            else:
                return default

    def finditer_with_line_numbers(self, pattern, string, flags=0):
        '''
        A version of 're.finditer' that returns '(match, line_number)' pairs.
        '''

        matches = list(re.finditer(pattern, string, flags))
        if not matches:
            # print('no matches')
            return {}

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

        for m in range(len(matches)):
            newline_offset = string.rfind('\n', 0, matches[m].start())
            newline_end = string.find('\n', matches[m].end())  # '-1' gracefully uses the end.
            line = string[newline_offset + 1:newline_end]
            line_number = newline_table[newline_offset]
            mList = [matches[m].group(), line_number, line]
            matcheslist.update({m:mList})

        return matcheslist
    
    def getSynonyms(self, line):
        l = line
        # synPatt = r'(?<={{syn\|ary\|)(.*?)(?=\<)'
        # syn2Patt = r'(?<=\|)(.*?)(?=\|)'
        # # newSynList = ""
        # if r"{{syn|" in line:
        #     l = "syn: " + self.reFindFirst(synPatt, l) + ', '
        #     if l != 'syn: ':
        #         return l
        #     sysList = self.reFindAll(syn2Patt, line)
        #     # print(sysList)
        #     l2 = "syn: "
        #
        #     for syn in sysList:
        #         # print("syn: " + syn)
        #         # r'[^؀-ۿ]'
        #         s = re.sub(r'[\u0600-\u06FF]', '',syn)
        #         print("syn:: " + s)
        #         if (s != ''):
        #             l2 += s + ", "
        #     l =l2

        # syn = ""
        if "{{syn|" in l:
            syn = r"(synonyms) "
            line = re.sub(r'[^\u0600-\u06FF\|]', '',l)
            line = line.replace('|', ' ')
            line = line.strip()
            # print(line)
            sList = list(line.split(" "))
            for s in sList:
                if s != "" and s != " " and s != "  " and s != "   " and s != "    ":
                    syn += s + ", "
            # print(syn)
            return syn + "; "

        return line
    
    def getAntonyms(self, line):
        l = line
      
        if "{{ant|" in l:
            syn = "(antonyms) "
            line = re.sub(r'[^\u0600-\u06FF\|]', '',l)
            line = line.replace('|', ' ')
            line = line.strip()
            # print(line)
            sList = list(line.split(" "))
            for s in sList:
                if s != "" and s != " " and s != "  " and s != "   " and s != "    ":
                    syn += s + ", "
            # print(syn)
            return syn + "; "

        return line

    def removeBlacklist(self, line):
        l = line

        prefix = "prefix"
        suffix = "suffix"

        blacklist = {
            1:{prefix:"{{senseid",suffix:"}}"},
            2:{prefix:"{{top",suffix:"}}"},
        }
        
        for value in blacklist.values():
            pref = value["prefix"]
            suff = value["suffix"]
            pattern = r'(?<='+pref+r')(.*?)(?='+suff+r')'
            matches = self.reFindAll(pattern, l)

            for m in matches:
                l = l.replace(pref+m+suff, '')

        return l
            
 
    # Clean wikiText template
    def cleanTemplate(self, line):
        l = line

        prefix = "prefix"
        suffix = "suffix"
        bkpSuffix = "bkpSuff"
        wrapin = "wrapin"

        cleanlist = {
            1:{prefix:'{{tlb|'+lng+'|',suffix:"}}", bkpSuffix:None, wrapin:"()"},
            2:{prefix:'{{uxi|'+lng+'|',suffix:"|", bkpSuffix:"}}", wrapin:" "},
            3:{prefix:'{{non-gloss',suffix:"|", bkpSuffix:None, wrapin: "()"},
        }
        
        for value in cleanlist.values():
            pref = value["prefix"]
            suff = value["suffix"]
            bkpSuff = value[bkpSuffix]
            wrap = value[wrapin]
            
            pattern = re.escape(pref)+r'(.*?)'+re.escape(suff)

            patternBkp = None
            if bkpSuff != None:
                patternBkp = re.escape(pref)+r'(.*?)'+re.escape(bkpSuff)
            # print(pattern)
            matches = self.reFindAll(pattern, l, patternBkp)
            # print(matches)

            for m in matches:
                m1 = m.replace('|', ',')
                if bkpSuff != None:
                    if wrap == "()":
                        l = re.sub(patternBkp, " (" +m1+ ") ", l)
                        # l = l.replace(pref+m+suff+bkpSuff, " (" + m1 + ") ")
                    else:
                        l = re.sub(patternBkp, " " +m1+ " ", l)
                        # l = l.replace(pref+m+suff+bkpSuff, " " + m1 + " ")
                else:
                    if wrap == "()":
                        l = re.sub(pattern, " (" +m1+ ") ", l)
                        # l = l.replace(pref+m+suff, ' (' + m1 + ') ')
                    else:
                        l = re.sub(pattern, " " +m1+ " ", l)
                        # l = l.replace(pref+m+suff, ' ' + m1 + ' ')

        return l    

    def getPlainLine(self, l):
        line = l
        line = self.getSynonyms(line)
        line = self.getAntonyms(line)
        line = self.removeBlacklist(line)
        line = self.cleanTemplate(line)
        
        lbPatt = r'(?<={{lb\|'+lng+r'\|)(.*?)(?=}})'
        ux2Patt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=}})'
        ux1Patt = r'(?<={{ux\|'+lng+r'\|)(.*?)(?=\|)'
        # glossPatt = r'(?<={{gloss\|)(.*?)(?=}})'

        lbMatchList = self.reFindAll(lbPatt, l)
        uxMatch = self.reFindFirst(ux1Patt, l)
        uxMatch2 = self.reFindFirst(ux2Patt, l)
        # glossMatchList = reH.reFindAll(glossPatt, l)
        
        # print(line)

        if len(lbMatchList) != 0:
            for m in lbMatchList:
                match = m
                match = match.replace('|', ', ')
                line = line.replace('{{lb|'+lng+'|'+ m +'}}', '(' + match + ')')
        
        if uxMatch != "":
            line = line.replace('{{ux|'+lng+'|'+ uxMatch2 +'}}', uxMatch)
        elif uxMatch2 != "":
            line = line.replace('{{ux|'+lng+'|'+ uxMatch2 +'}}', uxMatch2)
        
        # if len(glossMatchList) != 0:
        #     # print(uxMatchList)
        #     for m in glossMatchList:
        #         match = m
        #         line = line.replace('{{gloss|'+ m +'}}', match)

        ## The folowing two lines remove any other wikiText template
                
        linkPatt = r"\[\[(.*?)\]\]"

        linkList = re.findall(linkPatt, line)
        for link in linkList:
            # print(link)
            if "|" in link:
                # print("true")
                findOr = self.reFindFirst(r"^.*?\|", link)
                # print(findOr)
                line = line.replace("[[" +findOr, "")
            else:
                line = line.replace("[[" + link + "]]", link)

        # newPattr = re.compile(r"\[\[(.*?)|")
        
        # line = re.sub(r'\[^\]\}]/g', '', line)
        # line = line.replace(']', '')
        # line = line.replace("{{ux|"+lng+"|", "")
        line = line.replace("'''", "")
        line = line.replace("''", "")
        line = line.replace("{{q|", "")
        line = line.replace("{{gloss|", "")
        line = line.replace("{{m|"+lng+"|", "")
        
        restTempPattr = r'\{\{(.*?)\}\}'
        line = re.sub(restTempPattr, " ", line)

        # line = re.sub(r'[^a-zA-Z0-9\'(),;.\s]', '',line)
        line = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF\'(),;.\s]', '',line)
        # print("AFTER: "+line)

        return line


# line = "#: {{uxi|ary|ولد خاها|tr=wuld ḵāha|t=her fraternal nephew}}"
# reH = ReHelper()
#
# txt = reH.cleanTemplate(line)
# print(txt)
