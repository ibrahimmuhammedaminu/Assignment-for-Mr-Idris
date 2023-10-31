def find_pattern(input_string, pattern):
    result = []
    len_pattern = len(pattern)

    for i in range(len(input_string) - len_pattern + 1):
        if input_string[i:i + len_pattern] == pattern:
            result.append(i)

    return result

# Example usage:
input_string = "ABABABAABAABABAABABA"
pattern = "ABA"

matched_indexes = find_pattern(input_string, pattern)
print(f"Pattern '{pattern}' found at indexes: {matched_indexes}")



