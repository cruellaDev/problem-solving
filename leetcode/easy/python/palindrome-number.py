# https://leetcode.com/problems/palindrome-number/description/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
               
        answer = 0
        div = x
        while div != 0:
            div, mod = divmod(div, 10)
            answer = answer * 10 + mod
        return answer == x