# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/ 

from functools import reduce

def function(inputs):
    # function to get all subsets of a list using recursion
    def subset(nums):
        if not nums:
            return [[]]
        else:
            # slice off first element
            subsets = subset(nums[1:])
            return subsets + [[nums[0]] + x for x in subsets]
        
    # function to get the xor of all elements in a list
    def xor(nums):
        sum = 0
        for i in nums:
            if i:
                # used reduce to get the xor of all elements in the list
                result = reduce(lambda x, y: x ^ y, i)
            else:
                result = 0
            # add the result to the sum
            sum += result
        return sum
        
    all_subsets = subset(inputs)
    return xor(all_subsets)

# Test Case 1
input_1 = [1,3]
expected_output_1 = 6

# Test Case 2
input_2 = [5,1,6]
expected_output_2 = 28

# Test Case 3
input_3 = [3,4,5,6,7,8]
expected_output_3 = 480

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))