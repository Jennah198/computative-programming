class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(K):
            count = defaultdict(int)
            left = 0
            res = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    K -= 1
                count[nums[right]] += 1

                while K < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        K += 1
                    left += 1

                res += right - left + 1

            return res

        return atMost(k) - atMost(k - 1)