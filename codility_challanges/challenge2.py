max_int = 1000000


def solution(S: str, K: int):
    # write your code in Python 3.6
    if K > max_int and len(S) > max_int:
        raise ValueError("Error,  value beyond limit.")

    if K <= len(S):
        raise ValueError("Error, K should be less or equal to N!")

    compressed_str = ""
    freq = 1

    # Add the first char
    compressed_str += S[0]
    for letter in range(len(S) - 1):
        if S[letter] == S[letter + 1]:
            freq += 1
        else:
            if freq > 1:
                compressed_str += str(freq)
            else:
                compressed_str += S[letter+1]
                freq = 1
    if compressed_str > 1:
        compressed_str = str(freq)
    return compressed_str



