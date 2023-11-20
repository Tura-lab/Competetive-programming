class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(int)
        self.counts = defaultdict(int)
        self.past = defaultdict(str)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.past[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        past, time = self.past[id]
        time = t - time
        
        cur = (past, stationName)
        self.counts[cur] += 1
        self.times[cur] += time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cur = (startStation, endStation)
        return self.times[cur] / self.counts[cur]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)