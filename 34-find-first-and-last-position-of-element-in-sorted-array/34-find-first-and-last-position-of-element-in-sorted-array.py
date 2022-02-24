class Solution:
    def searchRange(self, nums, target):
        found = [None, None]
        l=0
        r = len(nums)-1
        
        def bs(l ,r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    if found[0] == None:
                        found[0] = mid
                    else:
                        found[0] = min(found[0], mid)
                    if found[1] == None:
                        found[1] = mid
                    else:
                        found[1] = max(found[1], mid)
                    bs(l,mid-1)
                    bs(mid+1,r)
                    return
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
        bs(0, len(nums)-1)
        if found == [None, None]:
            return [-1,-1]
        return found
            