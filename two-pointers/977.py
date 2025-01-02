# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/ 

def function(inputs):

    # naive approach
    # return sorted([i ** 2 for i in inputs])

    # two pointers approach
    left, right = 0, len(inputs) - 1
    result = [0] * len(inputs)
    pos = len(inputs) - 1

    while left <= right:
        # compare the squares of the two pointers and add the larger one to the extreme right of the result array
        if (inputs[left] ** 2) > (inputs[right] ** 2):
            result[pos] = inputs[left] ** 2
            left += 1
        else:
            result[pos] = inputs[right] ** 2
            right -= 1
        pos -= 1
    return result

# Test Case 1
input_1 = [-4,-1,0,3,10]
expected_output_1 = [0,1,9,16,100]

# Test Case 2
input_2 = [-7,-3,2,3,11]
expected_output_2 = [4,9,9,49,121]

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