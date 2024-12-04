# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/ 

def function(num):
    s, m = 0, 1

    # string method to solve the problem
    # for i in str(n):
    #     s = s + int(i)
    #     m = m * int(i)
    # return m - s

    # numerical method to solve the problem
    while num > 0:
        digit = num % 10
        num = num // 10
        s = s + digit
        m = m * digit
    return m - s

# Test Case 1
input_1 = 234
expected_output_1 = 15

# Test Case 2
input_2 = 4421
expected_output_2 = 21

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