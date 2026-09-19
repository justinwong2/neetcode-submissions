class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        positionSpeed = []
        fleet = 0
        for i in range(len(position)):
            timeRequired = float((target - position[i]) / speed[i])
            positionSpeed.append([position[i], speed[i], timeRequired])
        positionSpeed.sort()
        
        while len(positionSpeed) > 0:
            if len(positionSpeed) == 1:
                fleet += 1
                positionSpeed.pop()
                continue
            
            currLeader = positionSpeed.pop()
            while len(positionSpeed) > 0 and currLeader[2] >= positionSpeed[-1][2]:
                positionSpeed.pop()
            fleet += 1
        
        return fleet



