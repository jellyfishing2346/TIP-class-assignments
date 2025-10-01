def process_data(names, scores):
    result = {}
    for i in range(len(names)):
        name = names[i]
        score = scores[i]
        if name not in result:
            result[name] = []
        result[name].append(score)
    return result

names = ["Alice", "Bob", "Alice", "Bob", "Charlie"]
scores = [85, 90, 95, 80, 70]
result = process_data(names, scores)
print(result) # {'Alice': [85, 95], 'Bob': [90, 80], 'Charlie': [70]}