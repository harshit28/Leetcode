def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap = {x[0]: x for x in pieces}
        temp = []
        
        for elem in arr:
            temp += hashmap.get(elem, [])
return temp == arr
