from math import log, ceil

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        x = ceil(math.log(len(self.nums), 2))
        m = 2 ** x
        while len(self.nums) < m:
            self.nums.append(0)
        n = len(self.nums)
        
        self.tree = [0]*((2**(x+1))-1)
        l = len(self.tree)
        
        for i in range(n):
            self.tree[n+i-1] = self.nums[i]
            
        for i in range(n-2, -1, -1):
            self.tree[i] = self.tree[i*2+1] + self.tree[i*2+2]
        
        
        

    def update(self, index: int, val: int) -> None:
        index = len(self.nums) + index -1
        self.tree[index] = val
        
        while index:
            if index%2==0:
                index-=1
            index//=2
            self.tree[index] = self.tree[index*2+1] + self.tree[index*2+2]
        

    def sumRange(self, left: int, right: int) -> int:
        def f(l, r, cur):
            if r<left or l>right:
                return 0
            if l>=left and r<=right:
                return self.tree[cur]
            
            mid = l + (r-l)//2
            return f(l, mid, cur*2+1) + f(mid+1, r, cur*2+2)
        
        return f(0, len(self.nums)-1, 0)
            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)