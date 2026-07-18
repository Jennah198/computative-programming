class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            mid = (first + last) // 2
            
            if nums[mid] == target:
                return mid
                
            elif nums[mid] > target:
                last = mid - 1
                
            else:
                first = mid + 1
                
        return first


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna