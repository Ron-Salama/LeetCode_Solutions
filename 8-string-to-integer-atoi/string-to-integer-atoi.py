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
                if s[char] == '0':
                    temp = 0
                elif s[char] == '1':
                    temp = 1
                elif s[char] == '2':
                    temp = 2
                elif s[char] == '3':
                    temp = 3
                elif s[char] == '4':
                    temp = 4
                elif s[char] == '5':
                    temp = 5
                elif s[char] == '6':
                    temp = 6
                elif s[char] == '7':
                    temp = 7
                elif s[char] == '8':
                    temp = 8
                elif s[char] == '9':
                    temp = 9
                            
                result_as_integer = result_as_integer*10 + int(temp)
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
