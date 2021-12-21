class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_arr = sorted([(position[i],speed[i]) for i in range(len(speed))], key=lambda item:item[0])
        fleet_head = new_arr[-1]
        fleet = 0
        for i in range(len(new_arr)-1, -1, -1):
            t_available = (target-fleet_head[0])/fleet_head[1]
            if new_arr[i][1]<=fleet_head[1]:
                fleet_head=new_arr[i]
                fleet+=1
                continue
            t_needed = (fleet_head[0] - new_arr[i][0]) / (new_arr[i][1]-fleet_head[1])
            if t_needed<=t_available:
                continue
            else:
                fleet_head = new_arr[i]
                fleet+=1
        return fleet
