class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_dict = {}
        n=len(arr)
        tot=0
        removed = 0
        for num in arr:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        for num, count in count_dict.items():
            if tot>= n/2:
                break
            tot+=count
            removed+=1
        return removed
