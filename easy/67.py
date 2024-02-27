# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

def function(inputs):
    # convert the binary strings to integers
    a, b = int(inputs[0], 2), int(inputs[1], 2)
    sum = a + b
    return bin(sum)[2:]

# Test Case 1
input_1 = ["11","1"]
expected_output_1 = "100"

# Test Case 2
input_2 = ["1010","1011"]
expected_output_2 = "10101"

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))