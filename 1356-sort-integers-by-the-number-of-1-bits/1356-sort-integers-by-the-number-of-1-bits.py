class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(num):
            count = 0
            for i in range(32):
                if num & 1 << i:
                    count += 1
            
            return count
        
        counts = [(count_bits(num), num) for num in arr]
        
        return [num for count, num in sorted(counts)]