# 2697. Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/description/ 

def function(s):
    part = ''
    # iterate till the middle of the string
    for i in range(len(s)//2):
        # check if the characters at the i-th and last-i index are different
        if(s[i] != s[-1-i]):
            # append the minimum of the two characters. (lexicographically smallest one)
            part += chr(min(ord(s[i]), ord(s[-1-i])))
        else:
            part += s[i]

    # if the string is odd, then store the middle character to the string
    middle = s[len(s)//2] if(len(s) % 2 != 0) else ''
    
    # create the palindrome by concatenating the part, middle and the reversed part
    return (part+middle+part[::-1])

# Test Case 1
input_1 = "egcfe"
expected_output_1 = "efcfe"

# Test Case 2
input_2 = "abcd"
expected_output_2 = "abba"

# Test Case 3
input_3 = "seven"
expected_output_3 = "neven"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))