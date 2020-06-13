class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap={}
        ana=[]
        for s in strs:
            arr=sorted(list(s))
            elem="".join(arr)
            if elem in hashmap:
                indic=hashmap.get(elem)
                hashmap[elem]=indic + [s]
            else:
                hashmap[elem]= [s]
        for h in hashmap:
            if hashmap[h]:
                ana.append(hashmap.get(h))            
        return ana
