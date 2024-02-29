# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/ 

def function(inputs):
    result = []
    # Method 1: Naive Approach
    # for i in range(len(inputs)):
    #     result.append(sum(inputs[:i+1]))
    # return result

    # Method 2: One Liner Anonymous Function 
    return list(map(lambda x: sum(inputs[:x[0]+1]), enumerate(inputs)))

# Test Case 1
input_1 = [1,2,3,4]
expected_output_1 = [1,3,6,10]

# Test Case 2
input_2 = [1,1,1,1,1]
expected_output_2 = [1,2,3,4,5]

# Test Case 3
input_3 = [3,1,2,10,1]
expected_output_3 = [3,4,6,16,17]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))