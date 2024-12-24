# 3280. Convert Date to Binary
# https://leetcode.com/problems/convert-date-to-binary/description/ 

def binary(n):
    # recursive function to convert decimal to binary
    return '' if n <= 0 else binary(n // 2) + str(n % 2) 

def function(inputs):
    # one liner to convert date to binary
    # return '-'.join([bin(int(i)).replace('0b','') for i in inputs.split('-')])

    # manual method
    date = inputs.split('-')
    return '-'.join([binary(int(i))[1:] for i in date])

# Test Case 1
input_1 = "2080-02-29"
expected_output_1 = "100000100000-10-11101"

# Test Case 2
input_2 = "1900-01-01"
expected_output_2 = "11101101100-1-1"

# Test Case 3
input_3 = []
expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    # assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))