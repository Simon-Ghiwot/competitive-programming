class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        i = 0
        
        while i < len(source):
            block = source[i].find("/*")
            single = source[i].find("//") 
            if block == -1 and single == -1:
                if source[i]:
                    result.append(source[i])
            else:
                if block == -1:
                    index = source[i].find("//")
                    before_comment = source[i][0 : index]
                    if before_comment:
                        result.append(before_comment) 
                else:
                    if single == -1 or block < single:
                        index = source[i].find("/*")
                        before_comment = source[i][0 : index]
                        source[i] = source[i][index + 2: len(source[i])]
                        while source[i].find("*/") == -1:
                            i += 1
                        index = source[i].find("*/") + 2
                        after_comment = source[i][index : len(source[i])]
                        comment = before_comment + after_comment
                        source[i] = comment
                        continue
                    else:
                        index = source[i].find("//")
                        before_comment = source[i][0 : index]
                        if before_comment:
                            result.append(before_comment) 
            i += 1
        return result
