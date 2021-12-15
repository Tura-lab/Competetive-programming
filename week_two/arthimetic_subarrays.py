class Solution:
  def is_arthimetic(self, subarr):
      if len(subarr)<3:
          return True
      step = subarr[1]-subarr[0]
      for i in range(1,len(subarr)-1):
          if subarr[i] + step != subarr[i+1]:
              return False
      return True
  def checkArithmeticSubarrays(self,nums, l, r):
      bool_arr = []
      for i in range(len(l)):
          subarr = sorted(nums[l[i]:r[i]+1])
          bool_arr.append(self.is_arthimetic(subarr))
      return bool_arr
