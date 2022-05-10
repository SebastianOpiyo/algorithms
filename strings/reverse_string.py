"""A function that when given a string, reverses it"""

astring = "Sebastian"

def reverse_string(somestring:str)-> str:
    new_word = ""
    for letter in somestring[::-1]:
        new_word = new_word + letter
    return new_word


def palindrome(astring:str)-> str:
    reversed_word =  reverse_string(astring)
    if reversed_word == astring:
        return "Palindrome"
    return "Not Palindrome"


if __name__ == "__main__":
    # reverse_string(astring)
    astring = "madam"
    print(palindrome(astring))
    word = "chess"
    print(palindrome(word))