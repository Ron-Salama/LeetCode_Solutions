class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for char in s[::-1] :
            if char ==" " and count>0:
                break
            elif char != " ":
                count += 1
            
        return count

                