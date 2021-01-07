    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = []
        max_len = 0
        for char in s:
            if char not in hashset:
                hashset.append(char)
            else:
                if char == hashset[-1]:
                    hashset = []
                else:
                    index=hashset.index(char)
                    hashset = hashset[index+1:]
                hashset.append(char)
            max_len=max(max_len,len(hashset))
        return max_len
