import re

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

    
    
