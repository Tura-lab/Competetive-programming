class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        counter = Counter(ages)
        ages.sort()
        
        l = 0
        for i in range(len(ages)):
            if i+1 < len(ages) and ages[i] == ages[i+1]:continue
            while l < i and ages[l] <= 0.5 * ages[i] + 7:
                l += 1
            
            count += (i - l) * counter[ages[i]]
            
        return count