class Solution:
    '''
    1,6,12,12,14,14,17,17,3,8,11,7,4,11,18,8,8,3
    '''
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def findLIS(nums):
            def findPosAndReplace(num,s, e):
                mid = (s+e)//2
                # print(mid, LIS[mid], num)
                if LIS[mid] > num and (mid-1<0 or LIS[mid-1] <= num):
                    LIS[mid] = num
                    return
                if LIS[mid] > num:
                    findPosAndReplace(num,s,mid)
                else:
                    findPosAndReplace(num,mid,e)

            LIS = []
            for num in nums:
                if LIS==[] or num>=LIS[-1]:
                    LIS.append(num)
                else:
                    findPosAndReplace(num,0,len(LIS))
                # print(num,LIS)
            return len(LIS)
        
        i=0
        ans = 0
        while i < k:
            new = []
            n=i
            while n<len(arr):
                new.append(arr[n])
                n+=k
            ans += len(new)-findLIS(new)
            # print(new, findLIS(new) ,ans)
            i+=1
            
        return ans
        