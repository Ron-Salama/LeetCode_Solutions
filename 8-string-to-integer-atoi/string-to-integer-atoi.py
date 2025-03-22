class Solution(object):
    def myAtoi(self, s):
        result_as_integer = 0
        s = s.strip()
        sign = 0
        if(s==""):
            return 0
        
        if(s[0]=="-"):
            sign = -1
        elif(s[0]=="+"):
            sign = 1
        
        for char in range(abs(sign),len(s)):
            if(s[char].isdigit()):
                result_as_integer = result_as_integer*10 + int(s[char])
            else:
                break
        if(sign == 0):
            sign = 1
        result_as_integer = result_as_integer*sign

        if(result_as_integer>2**31 - 1):
            result_as_integer = 2**31 - 1
        elif(result_as_integer< -2**31):
            result_as_integer = -2**31

        return result_as_integer
