class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize: lowercase + extract words only
        words = re.findall(r"[a-z]+", paragraph.lower())

        banned_set = set(banned)
        counts = Counter()

        for word in words:
            if word not in banned_set:
                counts[word] += 1

        return counts.most_common(1)[0][0]