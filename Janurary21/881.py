class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count,i,j=0,0,len(people)-1
        print(j)
        while i<=j:
            count+=1
            if people[i] + people[j] <=limit:
                i+=1
            j-=1
        return count
