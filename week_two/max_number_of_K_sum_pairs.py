def maxOperations(self, nums: List[int], k: int) -> int:
    total=0
    count_dict= {}
    for num in nums:
        if num not in count_dict:
            count_dict[num]=1
        else:
            count_dict[num]+=1
    for num in nums:
        if k-num == num and num in count_dict and count_dict[num]>=2:
            total+=1
            count_dict[num]-=2
        elif k-num != num and k-num in count_dict and count_dict[k-num]>0 and count_dict[num]>0:
            total+=1
            count_dict[k-num]-=1
            count_dict[num]-=1
    return total
