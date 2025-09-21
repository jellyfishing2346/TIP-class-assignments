def mystery_function(word):

    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

word = "kayak"
result = mystery_function(word)
print(result) # True