# def Solution(N):
# Convert the +v int into binary
# zero_counter variable
# Check the max num of zeros within 1's by use of a loop
# return the max num if existing otherwise return 0

def solution(n):
    # checks for the correct value of n
    if not isinstance(n, int):
        raise TypeError("Only positive integer values accepted!")

    if n < 1 and (n > 2, 147, 483, 647):
        raise ValueError("Only positive values less than 2,147,483,647 are accepted!")

    binary_num = f'{n:b}'
    print(binary_num)

    # final_max_value = None
    # temp_max = None
    # for bin_0 in binary_num:
    #     if bin_0 == 0:
    #         pass
    # if final_max_value is not None:
    #     return final_max_value
    # else:
    #     return 0

    # Improved the solution below.
    return len(max(format(n, 'b').strip('0').split('1')))


print(solution(1053))
