def solution(s):
    string_len = len(s)
    possible_split = 0

    # Prefix and suffix array for to determine distinct char from
    # start and end
    prefix = [0] * string_len
    suffix = [0] * string_len

    freq = [0] * 26

    # Calculating prefix array
    for i in range(string_len):

        prev = prefix[i - 1] if (i - 1 >= 0) else 0

        # Character appears for 1st time in string
        if freq[ord(s[i]) - ord('a')] == 0:
            prefix[i] += (prev + 1)

        else:
            prefix[i] = prev
        freq[ord(s[i]) - ord('a')] = 1

    # Resetting seen for
    # suffix calculation
    freq = [0] * len(freq)

    # Calculating the suffix array
    suffix[string_len - 1] = 0
    for i in range(string_len - 1, 0, -1):
        prev = suffix[i]

        # char first appearance
        if freq[ord(s[i]) - ord('a')] == 0:
            suffix[i - 1] += (prev + 1)

        else:
            suffix[i - 1] = prev

        # char appeared
        freq[ord(s[i]) - ord('a')] = 1

    for i in range(string_len):
        if prefix[i] == suffix[i]:
            possible_split += 1

    return possible_split


# Driver Code 
if __name__ == "__main__":
    s = "ababab"

    print(solution(s))
