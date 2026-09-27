class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        checked = []
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            checked.append(trip)
        
        
        #since i filtered out all those that can burst the target, does it mean as long as the values exist it will be valid??
        #why? will there be a case where the merge order will matter??

        #ok by filtering the values that can exceed out, it means that if i merge all the ones that are left, each value will only be <= te target. which means the only time i fail is when all the values in the column is lesser than the target
        #there wont be a case where it fails because it exceeds.

        answer = [0,0,0]
        for t in checked:
            answer[0] = max(answer[0], t[0])
            answer[1] = max(answer[1], t[1])
            answer[2] = max(answer[2], t[2])
        
        return answer == target
         