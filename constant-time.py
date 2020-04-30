# Constant Time.

"""
- An algo is said to have Constant time when it is not depended on the imput data(n)
- No matter the size of input data, the running time will always be same."""

# Example 1:  (O(1))

def test_greater(a, b):
    if a > b:
        return True
    else:
        return False


# Example 2: (O(1))
# A function to get the first element in a list.
# How big the list is doesn't really matter as the first element will alway
# be returned in constant time.

def get_first(data_list):
    return data_list[0]

if __name__=='__main__':
    data_list = [20,40,67,89,35,76]
    print(get_first(data_list))
