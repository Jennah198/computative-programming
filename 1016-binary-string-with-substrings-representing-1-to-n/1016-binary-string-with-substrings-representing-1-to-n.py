class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # For numbers > len(s) * something, they can't be substrings
        # But we'll use a set approach
        
        found = set()
        L = len(s)
        
        # Check all substrings
        for i in range(L):
            # Start building number from position i
            num = 0
            for j in range(i, L):
                # Build binary number: num = num*2 + int(s[j])
                num = num * 2 + int(s[j])
                
                # If num > n, further extensions will be larger
                if num > n:
                    break
                    
                # If num > 0, add to found set
                if num > 0:
                    found.add(num)
        
        # Check if we found all numbers from 1 to n
        for i in range(1, n + 1):
            if i not in found:
                return False
        
        return True