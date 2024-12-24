# 942. DI String Match
# https://leetcode.com/problems/di-string-match/description/ 

def function(inputs):
    indexes = list(range(len(inputs)+1))
    result, left, right = [], 0, len(indexes)-1

    for i in inputs:
        # if the character is 'I', then we need to count the index of the left most element
        if 'I' == i:
            result.append(indexes[left])
            left += 1
        # if the character is 'D', then we need to count the index of the right most element
        else:
            result.append(indexes[right])
            right -= 1

    # return the result list + the difference between result list and indexes list
    return result + list(set(result) ^ set(indexes))

# Test Case 1
input_1 = "IDID"
expected_output_1 = [0,4,1,3,2]

# Test Case 2
input_2 = "III"
expected_output_2 = [0,1,2,3]

# Test Case 3
input_3 = "DDI"
expected_output_3 = [3,2,0,1]

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))