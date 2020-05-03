class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter=Counter(ransomNote)
        
        for note,count in ransomCounter.items():
            if note in magazine:
                if count>magazine.count(note):
                     return False
            else:
                return False
        return True    
