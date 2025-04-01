class Solution(object):
    def reverse(self, x):
        result = 0 
        sub = False
        if x < 0 :
            x *= -1
            sub = True
        y=str(x)
        mult = 10**(len(y)-1)
        for i in range(len(y)):
            result = result + mult * (x%10)
            x = x//10
            mult /= 10

        if result > ((2**31) -1) or result < -(2**31):
            return 0
        if sub :
            return result*-1
        return result