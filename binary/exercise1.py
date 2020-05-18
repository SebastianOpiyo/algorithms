# Python3 Solution for above problem: 

# This function asks for user input
# And checks if it a bianry digit or not, if not it will throw an error
def get_user_input():
    x = input('Enter the first binary string to compute: ')
    y = input('Enter the second binary string to compute: ')
    
    # The line below checks for valid entry of binary string to base 10
    while True:
        try:
            if int(x, 2) and int(y, 2):
                break
        except ValueError:
            print("Oops!  One of your input is not a valid binary number.  Try again...")
        break
    # We store the values in a dict as key:value pair
    entry = {}
    entry['x'] = x
    entry['y'] = y
    print(entry)
    return entry

# This function adds two binary 
# strings return the resulting string 
def add_binary_nums(x, y):
    max_len = max(len(x), len(y)) 

    x = x.zfill(max_len) 
    y = y.zfill(max_len) 
    
    # initialize the result 
    result = '' 
    
    # initialize the carry 
    carry = 0

    # Traverse the string 
    for i in range(max_len - 1, -1, -1): 
        r = carry 
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result 
        carry = 0 if r < 2 else 1	 # Compute the carry. 
    
    if carry !=0 : result = '1' + result 

    return result.zfill(max_len) 

# Print Function
def print_binary_results():
    user_input_results = get_user_input()
    x = user_input_results['x']
    y = user_input_results['y']
    result = print(add_binary_nums(x, y))
    return result

print_binary_results()

