def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for c, w in zip(pattern, words):
        if (c in char_to_word and char_to_word[c] != w) or (w in word_to_char and word_to_char[w] != c):
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    return True

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()

    for line in input_data:
        # Skip empty or improperly formatted lines
        if not line.strip():
            continue

        # Safely split the line
        try:
            pattern_str, sentence = line.split(",")
            pattern_str = pattern_str.strip().strip('"')
            sentence = sentence.strip().strip('"')
        except ValueError:
            print("Invalid input format:", line)
            continue

        result = word_pattern(pattern_str, sentence)
        outfile.write(str(result) + '\n')
    outfile.close()