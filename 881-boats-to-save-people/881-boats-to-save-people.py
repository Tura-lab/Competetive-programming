class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        count=0
        i=len(people)-1
        j=0
        while j<=i:
            if people[j]+people[i] <= limit :
                i-=1
            count+=1
            j+=1
        return count