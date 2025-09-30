def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()

    result = count_words(input_data)
    print(result)