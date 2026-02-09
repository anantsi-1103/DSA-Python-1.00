def brute_force_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i}")

# Example
text = "AABAACAADAABAABA"
pattern = "AABA"
brute_force_match(text, pattern)
