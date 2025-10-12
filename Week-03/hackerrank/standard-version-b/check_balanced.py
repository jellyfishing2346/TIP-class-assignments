def check_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            stack.pop()
    return not stack