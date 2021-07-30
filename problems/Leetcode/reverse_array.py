# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.extend([s.pop() for i in range(len(s))])
        print(s)

    def reverseString_mirror(self, s: list) -> None:
        """
        Mirror Image
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        print(s)


aa = Solution()
aa.reverseString(["h", "e", "l", "l", "o"])
aa.reverseString_mirror(["h", "e", "l", "l", "o"])
