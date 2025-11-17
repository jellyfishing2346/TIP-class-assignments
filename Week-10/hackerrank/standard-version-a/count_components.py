def count_components(adjacency_dict):
    # Write your code here
    visited = set()
    components = 0
    nodes = set(adjacency_dict.keys())

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for neighbor in adjacency_dict.get(curr, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

    for node in nodes:
        if node not in visited:
            dfs(node)
            components += 1

    return components

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read entire input from stdin
    input_data = sys.stdin.read().strip()
    
    # Split input into multiple dictionary strings by separating on empty lines
    dict_strings = input_data.split("\n\n")
    
    for dict_string in dict_strings:
        # Convert string to a dictionary using ast.literal_eval
        adjacency_dict = ast.literal_eval(dict_string.strip())
        
        # Compute the result for this adjacency dict
        result = count_components(adjacency_dict)
        
        # Write the result to the output
        fptr.write(str(result) + '\n')
    
    fptr.close()