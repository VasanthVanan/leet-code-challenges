# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/ 

def function(inputs):
    # Two-pointer approach
    left, right = 0, len(inputs) - 1
    max_value = 0
    while left < right:
        max_value = max(min(inputs[left], inputs[right]) * (right - left), max_value)
        if inputs[left] < inputs[right]:
            left += 1
        else:
            right -= 1
    return max_value

# Test Case 1
input_1 = [1,8,6,2,5,4,8,3,7]
expected_output_1 = 49

# Test Case 2
input_2 = [1,1]
expected_output_2 = 1

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