class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        if(len(s)==0):
            return True

        for char in t:
            if (char == s[i] ):
                i = i + 1
            if(i == len(s)):
                return True

        return False

        