class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,max_f = 0,0
        counts = defaultdict(int)

        for r, char in enumerate(s):
            counts[char] += 1
            max_f = max(max_f, counts[char])

            window_len = r - l + 1
            if window_len - max_f > k:
                removing = s[l]
                counts[removing] -= 1
                l += 1
                # max_f is out of date, but doesn't matter because it is impossible
                # to achieve a new best without reobtaining accuracy of max_f
            window_len = r - l + 1
        # Since we never shrink the window length, the end window length is the 
        # largest possibility we saw
        return window_len
