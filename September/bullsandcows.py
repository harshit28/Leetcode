#Time Complexity :O(n)
#Space Complextity: O(n)
#First loop finds all the bull values and also subtracts the value for the corresponding number, second loop finds the cow values which are not equalt to index values.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow,bull=0,0
        secretCount= Counter(secret)
        for i in range(len(guess)):
            if guess[i] in secretCount and secretCount[guess[i]] !=0:
                if secret[i] == guess[i]:
                    bull+=1
                    secretCount[guess[i]] -=1
        for i in range(len(guess)):
            if guess[i] in secretCount and secretCount[guess[i]] !=0:
                if secret[i] != guess[i]:
                    cow+=1
                    secretCount[guess[i]] -=1

        return str(bull)+'A'+str(cow)+'B'
