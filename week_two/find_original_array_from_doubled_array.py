class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count_dict = {}
        ori = []
        changed = sorted(changed)
        if len(changed)%2:
            return []
        for num in changed:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        for num in changed:
            if num == 0 and num in count_dict and count_dict[num]>=2:
                count_dict[num] -= 2
                ori.append(num)
            elif num!=0 and num in count_dict and num*2 in count_dict and count_dict[num] and count_dict[num*2]:
                count_dict[num] -= 1
                count_dict[num*2] -= 1
                ori.append(num)
        return ori if len(ori) == len(changed)//2 else []
