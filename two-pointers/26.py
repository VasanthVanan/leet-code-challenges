# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/ 

def function(inputs):

    # Two-pointer approach
    left, right = 1, 1
    while right < len(inputs):
        if inputs[right] != inputs[right-1]:
            inputs[left] = inputs[right]
            left += 1
        right += 1

    return inputs[:left]

# Test Case 1
input_1 = [1,1,2]
expected_output_1 = [1,2]

# Test Case 2
input_2 = [0,0,1,1,1,2,2,3,3,4]
expected_output_2 = [0,1,2,3,4]

# Test Case 3
input_3 = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
expected_output_3 = [1,2,3,4]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))