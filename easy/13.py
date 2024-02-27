# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

def function(s):

    sum = 0 # add up values
    compare = 1 # the last letter we compared to

    # create a dictionary of mapped letters : numbers
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}

    # reverse the string
    s = s[::-1]

    # iterate through the string
    for i in s:
        if(roman_dict[i] > compare or roman_dict[i] == compare):
            sum = sum + roman_dict[i]
            compare = roman_dict[i]
        if(roman_dict[i] < compare):
            sum = sum - roman_dict[i]
            compare = roman_dict[i]

    return sum

# Test Case 1
input_1 = 'MCMXCIV'
expected_output_1 = 1994

# Test Case 2
input_2 = 'III'
expected_output_2 = 3

# Test Case 3
input_3 = 'LVIII'
expected_output_3 = 58

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))