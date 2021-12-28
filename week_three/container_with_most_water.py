class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        max_area = 0
        while j>=i:
            current_rect = min(height[i], height[j]) * (j-i)
            max_area = max(max_area, current_rect)
            if height[i]<height[j]:
                k=i+1
                while k<j:
                    if height[k] > height[i]:
                        i=k
                        break
                    k+=1
                if k==j:
                    break
            elif height[j]<height[i]:
                k=j-1
                while k>i:
                    if height[k] > height[j]:
                        j=k
                        break
                    k-=1
                if k==i:
                    break
            else:
                k = i+1
                l = j-1
                while k<j and l>i:
                    if height[l] > height[j]:
                        j=l
                        break
                    if height[k] > height[i]:
                        i=k
                        break
                    l-=1
                    k+=1
                if k==j or l==i:
                    break
        return max_area        
        
        
        #TLE
        # ans = 0
        # n = len(height)
        # right_bound_arr = []
        # left_bound_arr = []
        # left_bound_idx = 0
        # right_bound_idx = n-1
        # i = left_bound_idx
        # j = right_bound_idx
        # for i in range(len(height)):
        #     j = 0 
        #     while j<=i:
        #         if height[j] >= height[i]:
        #             left_bound_arr.append(j)
        #             break
        #         j+=1
        #     j = n-1
        #     while j>=i:
        #         if height[j] >= height[i]:
        #             right_bound_arr.append(j)
        #             break
        #         j-=1 
        # for i in range(len(height)):
        #     rect = min(height[left_bound_arr[i]], height[right_bound_arr[i]]) * (right_bound_arr[i] - left_bound_arr[i])
        #     if ans < rect:
        #         ans = rect
        # return ans
