# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/description/ 

def function(inputs):
    answer = []
    for i in range(len(inputs)):
        # calculate the difference between the sums of the first i and last n-i elements
        answer.append(abs(sum(inputs[:i]) - sum(inputs[i+1:])))
    return answer

# Test Case 1
input_1 = [10,4,8,3]
expected_output_1 = [15,1,11,22]

# Test Case 2
input_2 = [1]
expected_output_2 = [0]

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