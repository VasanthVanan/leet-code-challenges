# 2894. Divisible and Non-divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/ 

def function(inputs):
    n, m = inputs[0], inputs[1]

    # arithmetic sum formula
    total = n * (n + 1) // 2
    # largest integer divisible by m
    k = n // m
    # arithmetic sum divisible by m formula
    num2 = m * (k * (k + 1)) // 2

    # return the difference
    return (total - num2) - num2
    
# Test Case 1
input_1 = [10,3]
expected_output_1 = 19

# Test Case 2
input_2 = [5,6]
expected_output_2 = 15

# Test Case 3
input_3 = [5,1]
expected_output_3 = -15

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))