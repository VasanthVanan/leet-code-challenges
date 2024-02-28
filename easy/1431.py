# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/ 

def function(inputs):
    maximum = max(inputs[0])
    result = []

    for i in inputs[0]:
        r = True if i + inputs[1] >= maximum else False
        result.append(r)

    return result

# Test Case 1
input_1 = [[2,3,5,1,3], 3]
expected_output_1 = [True,True,True,False,True] 

# Test Case 2
input_2 = [[4,2,1,1,2], 1]
expected_output_2 = [True, False, False, False, False]

# Test Case 3
input_3 = [[12,1,12], 10]
expected_output_3 = [True, False, True]

# Test Case 4
input_4 = [[2,3,5,1,3], 3]
expected_output_4 = [True,True,True,False,True]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    assert function(input_4) == expected_output_4, f'Test Case 4 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))