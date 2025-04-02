class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        numbers = ["", "", ["a", "b", "c"], ["d", "e", "f"], 
                   ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], 
                   ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        
        def backtrack(index, path):
            if index == len(digits):
                output.append("".join(path))
                return
            
            digit = int(digits[index])
            for letter in numbers[digit]:
                backtrack(index + 1, path + [letter])

        output = []
        backtrack(0, [])
        return output
