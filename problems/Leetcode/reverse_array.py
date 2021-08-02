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

    def reverseString_two_pointers(self, s: list) -> None:

        # one points to head position, the other points to tail position
        left, right = 0, len(s)-1

        # reverse string by two pointers
        while left < right:

            s[left], s[right] = s[right], s[left]

            left, right = left+1, right-1
        print(s)

    def reverseString_recurse(self, s: list) -> None:

        def helper(left: int, right: int, string: list):

            if left >= right:
                # base case
                return

            # general case
            s[left], s[right] = s[right], s[left]

            helper(left+1, right-1, s)
        # ------------------------------------------------

        helper(left=0, right=len(s)-1, string=s)
        print(s)


aa = Solution()
aa.reverseString(["h", "e", "l", "l", "o"])
aa.reverseString_mirror(["h", "e", "l", "l", "o"])
aa.reverseString_two_pointers(["H", "a", "n", "n", "a", "h"])
aa.reverseString_recurse(["H", "a", "n", "n", "a", "h"])
