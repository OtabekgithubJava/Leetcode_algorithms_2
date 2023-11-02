class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combinations = []

        def backtrack(combination, next_digits):

            if len(next_digits) == 0:
                combinations.append(combination)
            else:
                letters = digit_to_letters[next_digits[0]]
                for letter in letters:
                    backtrack(combination + letter, next_digits[1:])

        backtrack('', digits)
        return combinations

class Solution(object):
    def generateParenthesis(self, n):
        combinations = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                combinations.append(s)
                return

            if left < n:
                backtrack(s + '(', left + 1, right)

            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack('', 0, 0)
        return combinations


class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        word_len = len(words[0])
        total_len = len(words) * word_len
        result = []

        for i in range(len(s) - total_len + 1):
            substring = s[i:i + total_len]
            substring_count = {}

            for j in range(0, total_len, word_len):
                word = substring[j:j + word_len]
                substring_count[word] = substring_count.get(word, 0) + 1

            if substring_count == word_count:
                result.append(i)

        return result



class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0

        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result