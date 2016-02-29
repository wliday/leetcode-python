class Solution(object):
    def reverseWords(self, s):
        if not s: return None

        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i - 1)
                beg = i + 1
            elif i == len(s) - 1:
                self.reverse(s, beg, i)

    def reverse(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1