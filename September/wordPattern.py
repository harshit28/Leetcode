class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False
        strList = str.split(" ")
        hashmap={}
        if len(strList) != len(pattern):
            return False
        for i in range(len(strList)):
            if pattern[i] not in hashmap:
                if strList[i] not in hashmap.values():
                    hashmap[pattern[i]] = strList[i]
                else:
                    return False
            else:
                if hashmap[pattern[i]]!=strList[i]:
                    return False
        return True
