# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/description/ 

def function(inputs):
    for i in range(len(inputs)):
        # reverse the row by slicing
        inputs[i] = inputs[i][::-1]
    
    for i in range(len(inputs)):
        # inverse with if else condition
        #inputs[i] = [1 if x == 0 else 0 for x in inputs[i]]
        # inverse with bitwise XOR operator
        inputs[i] = [1 ^ x for x in inputs[i]]

    return inputs

# Test Case 1
input_1 = [[1,1,0],[1,0,1],[0,0,0]]
expected_output_1 = [[1,0,0],[0,1,0],[1,1,1]]

# Test Case 2
input_2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
expected_output_2 = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

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