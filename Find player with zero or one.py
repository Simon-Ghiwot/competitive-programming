class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = []
        winner = {}
        loser = {}
        for i in range(len(matches)):
            winner[matches[i][0]] = winner.get(matches[i][0], 0) + 1
            loser[matches[i][1]] = loser.get(matches[i][1], 0) + 1
        zero, one = [], []
        for key in winner.keys():
            if key not in loser:
                zero.append(key)
        zero.sort()
        result.append(zero);
        for key in loser.keys():
            if loser[key] == 1:
                one.append(key);
        one.sort()
        result.append(one)
        return result;
