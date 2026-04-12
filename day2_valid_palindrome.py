#Given a string, determine if it's a palindrome — 
# meaning it reads the same forwards and backwards. 
# Only consider letters and numbers (ignore spaces, punctuation, etc.), 
# and treat uppercase and lowercase as the same.


def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right and not s[left].isalnum():
        left+=1
    while left < right and not s[right].isalnum():
        right+=1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1       
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))

