# 2367. Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/description/ 

def function(inputs):
    nums, diff = inputs[0], inputs[1]
    count = 0
    # O(n^3) time complexity
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # checks if the difference between i and j is diff
            if(nums[j] - nums[i] == diff):
                for k in range(j+1, len(nums)):
                    # checks if the difference between j and k is diff
                    if(nums[k] - nums[j] == diff):
                        count += 1

    return count

# Test Case 1
input_1 = [[0,1,4,6,7,10],3]
expected_output_1 = 2

# Test Case 2
input_2 = [[4,5,6,7,8,9],2]
expected_output_2 = 2

# Test Case 3
input_3 = []
expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))