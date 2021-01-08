    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        output = []
        arrayA,arrayB= A.split(" "), B.split(" ")
        count ={}
        for char in arrayA:
            count[char] = count.get(char,0) + 1
         
        
        for char in arrayB:
            count[char] = count.get(char,0) + 1
            
                
        return [word for word in count if count[word]==1]
