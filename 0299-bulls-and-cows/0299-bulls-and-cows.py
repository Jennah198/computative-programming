class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count = [0] * 10  # net count: +1 for secret, -1 for guess
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_digit = int(s)
                g_digit = int(g)
                
                # If we've seen this digit in guess before (count < 0), it's a cow
                if count[s_digit] < 0:
                    cows += 1
                # If we've seen this digit in secret before (count > 0), it's a cow
                if count[g_digit] > 0:
                    cows += 1
                
                count[s_digit] += 1
                count[g_digit] -= 1
        
        return f"{bulls}A{cows}B"