class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = Counter(nums1)
        res = []

        for x in nums2:
            if count[x] > 0:
                res.append(x)
                count[x] -= 1

        return res