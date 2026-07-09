from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = list()
        types = list()
        
        for s in strs:
            if Counter(s) in types:
                idx = types.index(Counter(s))
                answer[idx].append(s)
            else:
                answer.append([s])
                types.append(Counter(s))

        return(answer)