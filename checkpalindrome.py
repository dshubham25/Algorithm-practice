from collections import defaultdict
def checkPalindrome(n):
    char_count = defaultdict(int)
    for c in n:
        char_count[c] += 1
    odd_char = ""
    Palindrome = ""

    for c, cnt in char_count.items():
        if cnt % 2 == 0:
            Palindrome += c * (cnt//2)
        elif not odd_char:
            odd_char = c
            Palindrome += c * (cnt//2)

        else:
            return None
    return Palindrome + odd_char + Palindrome[::-1]
print(checkPalindrome("momom"))
print(checkPalindrome("qqaaaocle"))
