from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        # Impossible if one character is too frequent
        if max(freq.values()) > (n + 1) // 2:
            return ""

        res = [""] * n
        idx = 0

        # Place characters in descending frequency order
        for ch, count in sorted(freq.items(), key=lambda x: -x[1]):
            for _ in range(count):
                if idx >= n:
                    idx = 1  # switch to odd positions
                res[idx] = ch
                idx += 2

        return "".join(res)