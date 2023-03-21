class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = defaultdict(int)
        max_, max_person = -1, -1
        self.winner = []
        for i in range(len(times)):
            count[persons[i]] += 1
            if max_ <= count[persons[i]]:
                max_ = count[persons[i]]
                max_person = persons[i]

            self.winner.append([max_person, times[i]])

    def q(self, t: int) -> int:
        left, right = 0, len(self.winner) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.winner[mid][1] > t:
                right = mid - 1
            else:
                left = mid + 1
        return self.winner[left - 1][0]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
