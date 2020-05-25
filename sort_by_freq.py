class Solution:
    def frequencySort(self, s: str) -> str:
        s,dic="",Counter(s)
        for elem,index in dic.most_common():
                s+=elem * index
        return s
            

        
