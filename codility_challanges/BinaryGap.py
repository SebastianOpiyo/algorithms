# def Solution(N):
# Convert the +v int into binary
# zero_counter variable
# Check the max num of zeros within 1's by splitting the binary
# return the max num if existing otherwise return 0

# Solution 1: Best solution.
def solution(n):
    # checks for the correct value of n
    bin_limit = 2147483647
    if not isinstance(n, int):
        raise TypeError("Only positive integer values accepted!")

    if 1 > n:
        raise ValueError("Only positive values less than 2,147,483,647 are accepted!")

    if n > bin_limit:
        raise ValueError("Integer beyond limit!")

    # convert n to binary string
    # and strip off any hanging zeros at the end of it.
    binary_num = f'{n:b}'.strip('0')

    # get the list of zeros
    list_of_zeros = binary_num.split('1')
    # Get the len of max zeros
    max_value = len(max(list_of_zeros))
    # take care of lack of zero
    if max_value == '':
        return 0
    else:
        return max_value


# # 2. Condensed and less readable.
# def solution(n):
#     return len(max(format(n, 'b').strip('0').split('1')))

number = 2147483647
print(solution(number))
