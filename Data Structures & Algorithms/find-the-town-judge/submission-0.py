class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #if trust means there is an edge pointing to it
        #for a town judge, he should not have any outward edges because he trusts nobody
        #since there are n people, he should have n-1 edges pointing to him (since he doesnt trust himself)
        #if there is no clear candidate return -1
        #what algo is this? some topological one??
        #[0,0] people that trust this guy, people that this guy trusts
        people = [[0, 0] for _ in range(n + 1)]
        for i in range(len(trust)):
            truster = trust[i][0]
            trusted = trust[i][1]
            people[truster][1] += 1
            people[trusted][0] += 1

        for i in range(1, len(people)):
            curr = people[i]
            if curr[0] == (n-1) and curr[1] == 0:
                return i
        return -1        