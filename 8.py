class Solution(object):
    def myAtoi(self, str):
        if not str: return 0
        ls = list(str.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]

        res = 0
        for i in range(len(ls)):
            if ls[i].isdigit():
                res = res * 10 + ord(ls[i]) - ord('0')
            else:
                break

        return max(-2**31, min(sign * res, 2**31 - 1))