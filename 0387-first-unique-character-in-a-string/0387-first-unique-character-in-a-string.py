class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Array to store: [count, first_index]
        # Using large index as marker for not seen
        info = [[0, -1] for _ in range(26)]
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if info[idx][1] == -1:  # First time seeing this character
                info[idx][1] = i
            info[idx][0] += 1
        
        # Find minimum index with count = 1
        min_index = float('inf')
        for count, index in info:
            if count == 1 and index < min_index:
                min_index = index
        
        return min_index if min_index != float('inf') else -1