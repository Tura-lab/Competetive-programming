class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        '''
        ans = []
        cur_blooming = [10]
        [1,10],[3,3]
                 ^
        
        [2, 3, 3]
         ^
        '''
        
        cur_blooming = []
        ans = [0] * len(people)
        
        for i in range(len(people)):
            people[i] = (people[i], i)
            
        people.sort()
        flowers.sort()
        
        j = 0
        for i in range(len(people)):
            person, idx = people[i]
            while j < len(flowers) and flowers[j][0] <= person:
                heappush(cur_blooming, flowers[j][1])
                j += 1
                
            while cur_blooming and cur_blooming[0] < person:
                heappop(cur_blooming)
                
            ans[idx] = len(cur_blooming)
            
        return ans