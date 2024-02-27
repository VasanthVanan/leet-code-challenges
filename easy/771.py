# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

def function(inputs):
    a, b = inputs[0], inputs[1]
    # iterate through the string and count the number of jewels by using set and intersection
    return sum(1 for c in b if c in (set(a) & set(b)))
    


# Test Case 1
input_1 = ["aA","aAAbbbb"] 
expected_output_1 = 3

# Test Case 2
input_2 = ["z", "ZZ"]
expected_output_2 = 0

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))