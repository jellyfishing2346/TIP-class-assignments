def sum_matrix(matrix):
    row_length = len(matrix[0]) 
    total = 0
    for row in matrix:
        for j in range(row_length):
            total += row[j]
    return total

result = sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)  # Output: 45