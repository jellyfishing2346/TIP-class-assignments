def has_cycle(adj_matrix):
    # Write your code here
    visited = set()
    n = len(adj_matrix)

    def dfs(v, parent):
        visited.add(v)
        for neighbor in range(n):
            if adj_matrix[v][neighbor] == 1:  # There is an edge
                if neighbor not in visited:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read entire input from stdin
    input_data = sys.stdin.read().strip()
    
    # Split input into multiple dictionary strings by separating on empty lines
    dict_strings = input_data.split("\n\n")
    
    for dict_string in dict_strings:
        # Convert string to a dictionary using ast.literal_eval
        adj_matrix = ast.literal_eval(dict_string.strip())
        
        # Compute the result for this adjacency dict
        result = has_cycle(adj_matrix)
        
        # Write the result to the output
        fptr.write(str(result) + '\n')
    
    fptr.close()