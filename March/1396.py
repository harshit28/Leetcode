class UndergroundSystem:

    def __init__(self):
        self.hashmap = {}
        self.avgmap={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
            self.hashmap[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
            [start,time] = self.hashmap[id]
            duration = t - time
            if (start,stationName) not in self.avgmap: 
                self.avgmap[(start,stationName)] = (duration,1)
            else:
                curAvg,curCount = self.avgmap[(start,stationName)]
                average= (curAvg * curCount + duration) / (curCount + 1)
                self.avgmap[(start,stationName)] = (average,curCount+1)
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
           avg,count=self.avgmap[(startStation,endStation)]
           return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
