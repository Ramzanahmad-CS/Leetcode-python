class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start, end = 0, 0
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > end - start:
                    start, end = l + 1, r
        return s[start:end]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # bab (or aba)
    print(sol.longestPalindrome("cbbd"))   # bb
    print(sol.longestPalindrome("a"))      # a
    print(sol.longestPalindrome("ac"))     # a
