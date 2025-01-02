# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/ 

def function(inputs):
    #  Two-pointer approach
    numbers, target = inputs[0], inputs[1]
    left, right = 0, len(numbers) - 1
    while left < right:
        # if the sum of the two numbers is equal to the target, return the indices
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        # if the sum of the two numbers is less than the target, increment the left pointer
        elif numbers[left] + numbers[right] < target:
            left += 1
        # else, decrement the right pointer
        else:
            right -= 1

# Test Case 1
input_1 = [[2,7,11,15],9]
expected_output_1 = [1,2]

# Test Case 2
input_2 = [[2,3,4], 6]
expected_output_2 = [1,3]

# Test Case 3
input_3 = [[-1,0], -1]
expected_output_3 = [1,2]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))