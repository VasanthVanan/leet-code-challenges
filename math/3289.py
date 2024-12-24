# 3289. The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/ 

def function(inputs):
    hashmap = {}
    result = set()

    # iterate through the array
    for i in inputs:
        if i in hashmap:
            # if sneaky number found, add it to the result set
            result.add(i)
        else:
            hashmap[i] = 1
            
    # convert the set to list
    return list(result)

# Test Case 1
input_1 = [0,1,1,0]
expected_output_1 = [0,1]

# Test Case 2
input_2 = [0,3,2,1,3,2]
expected_output_2 = [2,3]

# Test Case 3
input_3 = [7,1,5,4,3,4,6,0,9,5,8,2]
expected_output_3 = [4,5]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))