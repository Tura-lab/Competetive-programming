class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = {l[i] : i+1 for i in range(len(l))}
        
        colNum = 0
        
        for let in columnTitle:
            colNum = colNum*26 + nums[let]
            
        return colNum