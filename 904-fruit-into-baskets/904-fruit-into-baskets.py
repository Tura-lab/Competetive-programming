class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        j=0
        counter = {}
        max=1
        while j<len(fruits):
            if len(counter)>=3:
                if counter[fruits[i]]==1:
                    del counter[fruits[i]]
                else:
                    counter[fruits[i]]-=1
                i+=1
            if fruits[j] in counter:
                counter[fruits[j]]+=1
            else:
                counter[fruits[j]]=1
            j+=1
        return j-i-1 if len(counter)>2 else j-i