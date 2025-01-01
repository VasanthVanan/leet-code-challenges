# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/ 

def function(nums):
    maximum_sum = current_sum = nums[0]

    for i in range(1,len(nums)):
        # Kadane's Algorithm
        current_sum = max(nums[i], current_sum + nums[i])
        if current_sum > maximum_sum:
            maximum_sum = current_sum
    
    return maximum_sum

# Test Case 1
input_1 = [-2,1,-3,4,-1,2,1,-5,4]
expected_output_1 = 6

# Test Case 2
input_2 = [1]
expected_output_2 = 1

# Test Case 3
input_3 = [5,4,-1,7,8]
expected_output_3 = 23

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))