# 3065. Minimum Operations to Exceed Threshold Value
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/

def function(inputs):
    nums, k = inputs[0], inputs[1]
    return len(nums) - len(list(filter(lambda x: x >= k, nums)))

# Test Case 1
input_1 = [[2,11,10,1,3],10]
expected_output_1 = 3

# Test Case 2
input_2 = [[1,1,2,4,9],1]
expected_output_2 = 0

# Test Case 3
input_3 = [[1,1,2,4,9],9]
expected_output_3 = 4

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))