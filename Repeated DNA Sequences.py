class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        store, ans = set(), set()
        for i in range(0, len(s) - 9):
            if s[i : i + 10] in store:
                ans.add(s[i : i + 10])
            else:
                store.add(s[i : i + 10])

        return list(ans)
