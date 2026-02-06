#brute force
def generateParenthesis(self, n):
    res = []

    def isValid(s):
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def generate(s):
        if len(s) == 2 * n:
            if isValid(s):
                res.append(s)
            return
        generate(s + '(')
        generate(s + ')')

    generate("")
    return res


#optimized
def generateParenthesis(self, n):
    res = []

    def backtrack(open_cnt, close_cnt, path):
        if len(path) == 2 * n:
            res.append(path)
            return

        if open_cnt < n:
            backtrack(open_cnt + 1, close_cnt, path + '(')

        if close_cnt < open_cnt:
            backtrack(open_cnt, close_cnt + 1, path + ')')

    backtrack(0, 0, "")
    return res
