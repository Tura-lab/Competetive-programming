class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr = [-1]
        mx = 0
        for i in range(len(heights)):
            while len(arr)>1 and heights[arr[-1]] > heights[i]:
                if mx < heights[arr[-1]] * ((i-1)-arr[-2]):
                    mx = heights[arr[-1]] * ((i-1)-arr[-2])
                arr.pop()
            arr.append(i)
        for i in range(1, len(arr)):
            if mx < heights[arr[i]] *(arr[-1]-arr[i-1]):
                mx = heights[arr[i]] *(arr[-1]-arr[i-1])
        return mx
        
        
        
        
        # mx = 0
        # for i in range(len(heights)):
        #     j=i-1
        #     possible = 1
        #     while j>-1 and heights[j]>=heights[i]:
        #         possible+=1
        #         j-=1
        #     j=i+1
        #     while j<len(heights) and heights[j]>=heights[i]:
        #         possible+=1
        #         j+=1
        #     if possible*heights[i] >mx:
        #         mx = possible*heights[i]
        # return mx