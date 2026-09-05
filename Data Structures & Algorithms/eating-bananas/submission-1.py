class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        left = 1
        right = max(piles)

        def timeTaken(piles, eatingRate):

            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/eatingRate)
            return hours
        
        while left <= right:
            middle = left + (right - left) // 2
            currentTime = timeTaken(piles, middle)
            if currentTime <= h: #still have buffer
                right = middle
            elif currentTime > h: #taking too long, need to speed up
                if left == middle:
                    middle += 1
                    break
                left = middle
        
        return middle

