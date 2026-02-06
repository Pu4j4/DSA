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
