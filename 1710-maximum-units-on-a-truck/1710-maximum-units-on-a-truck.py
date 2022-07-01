class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        
        total_units = total_boxes = 0
        # print(boxTypes)
        for i,j in boxTypes:
            num = min(i, truckSize-total_boxes)
            
            total_boxes += num
            total_units += num*j
            
        return total_units