# 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/ 

def function(inputs):
    n = len(inputs)
    total_sum = 0
    # O(n^2) time complexity
    # for i in range(n):
    #     for j in range(i, n):
    #         # if the length of the subarray is odd, add the sum of the subarray to total_sum
    #         if((j+1-i) % 2 == 1):    
    #             subarray = inputs[i:j+1]
    #             total_sum += sum(subarray)

    # O(n) time complexity - Two pointers method
    for i in range(n):
        left = i + 1
        right = n - i
        sums = (left * right + 1) // 2 * inputs[i]
        total_sum += sums
    return total_sum

# Test Case 1
input_1 = [1,4,2,5,3]
expected_output_1 = 58

# Test Case 2
input_2 = [1,2]
expected_output_2 = 3

# Test Case 3
input_3 = [10,11,12]
expected_output_3 = 66

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))