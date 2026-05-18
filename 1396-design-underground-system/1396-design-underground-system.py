class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.completed = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkedIn[id][0]
        startTime = self.checkedIn[id][1]
        if (startStation, stationName) not in self.completed:
            self.completed[(startStation, stationName)] = []
        self.completed[(startStation, stationName)].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.completed[(startStation, endStation)]
        return sum(times)/len(times)
    

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)