class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        used = [False] * len(nums)
        used_cnt = 0
        for i in range(len(nums)):
            if used[i]:
                continue
            seq, prev, prev_freq = 1, nums[i], freq[i]
            freq[prev] -= 1
            used[i] = True
            for j in range(i + 1, len(nums)):
                if prev == nums[j] or used[j]:
                    continue
                if freq[prev] >= freq[nums[j]] or nums[j] - 1 != prev:
                    break
                freq[nums[j]] -= 1
                prev_freq = freq[nums[j]]
                prev = nums[j]
                used[j] = True
                seq += 1
            if seq < 3:
                return False
        return True

        
