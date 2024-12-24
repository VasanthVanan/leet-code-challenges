# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/ 

def function(inputs):
    nums, target = inputs[0], inputs[1]
    left = 0
    final = float('inf')
    total = 0

    # sliding window approach
    for right in range(len(nums)):
        total += nums[right]
        # while loop to shrink the window
        while total >= target:
            total = total - nums[left]
            final = min(final, right - left + 1)
            left = left + 1

    return 0 if final == float('inf') else final

# Test Case 1
input_1 = [[2,3,1,2,4,3], 7]
expected_output_1 = 2

# Test Case 2
input_2 = [[1,4,4], 4]
expected_output_2 = 1

# Test Case 3
input_3 = [[1,1,1,1,1,1,1,1], 11]
expected_output_3 = 0

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))