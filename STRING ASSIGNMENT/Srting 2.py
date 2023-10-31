def find_pattern(input_string, pattern):
    result = []
    len_pattern = len(pattern)

    for i in range(len(input_string) - len_pattern + 1):
        if input_string[i:i + len_pattern] == pattern:
            result.append(i)

    return result

def replace_pattern(input_string, pattern, replacement):
    len_pattern = len(pattern)
    result = ''

    for i in range(len(input_string)):
        if input_string[i:i + len_pattern] == pattern:
            result += replacement
            i += len_pattern - 1
        else:
            result += input_string[i]

    return result

# Example usage:
input_string = "IBRAHIM MUHAMMED AMINU"
pattern = "slant"
replacement = "slant"

matched_indexes = find_pattern(input_string, pattern)
print(f"Pattern '{pattern}' found at indexes: {matched_indexes}")

replaced_string = replace_pattern(input_string, pattern, replacement)
print(f"String after replacement: {replaced_string}")




