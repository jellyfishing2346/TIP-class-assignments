def check_palindrome(s):
    # Write your code here
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

result = check_palindrome("racecar")
print(result)  # Output: True