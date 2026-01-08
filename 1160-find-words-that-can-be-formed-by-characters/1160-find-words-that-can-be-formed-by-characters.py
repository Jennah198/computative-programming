class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
            for c in word_count:
                if word_count[c] > char_count[c]:
                    break
            else:
                total += len(word)

        return total