def letter_comb(digits):
    if not digits:
        return []
    phone = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }
    result = [""]
    for digit in digits:
        temp = []
        for combo in result:
            for ch in phone[digit]:
                temp.append(combo+ch)
        result = temp
    return result

digits = "32"
print(letter_comb(digits))

