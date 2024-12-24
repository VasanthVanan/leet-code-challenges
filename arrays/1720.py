# 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/description/ 

def function(inputs):
    encoded, result = inputs[0], [inputs[1]]
    for i, x in enumerate(encoded):
        # XOR the current element of encoded with the previous element in result
        result.append(result[i] ^ x)
    return result

# Test Case 1
input_1 = [[1,2,3], 1]
expected_output_1 = [1,0,2,1]

# Test Case 2
input_2 = [[6,2,7,3], 4]
expected_output_2 = [4,2,0,7,4]

# Test Case 3
input_3 = [[1], 1]
expected_output_3 = [1, 0]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))