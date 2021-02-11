class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_array = [0] * 256
        
        for char in s:
            char_array[ord(char)] +=1
        for char in t:
            if char_array[ord(char)] ==0:
                return False
            char_array[ord(char)] -=1


        
        return True if not sum(char_array) else False
