class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            arr = dic.get(temp, [])
            arr.append(i)
            dic[temp] = arr

        answer = []
        for key, value in dic.items():
            temp = []
            for j in value:
                temp.append(strs[j])
            answer.append(temp)
        return answer

        