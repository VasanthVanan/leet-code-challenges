# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/description/ 

def function(inputs):
    count = 0
    # naive method
    # for i in range(len(inputs)):
    #     for j in range(i+1, len(inputs)):
    #         count = count + 1 if inputs[i] == inputs[j] else count
    # return count

    hashmap = {}
    # optimized method
    for i in inputs:
        # if the number is not in the hashmap, add it to the hashmap
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] = hashmap[i] + 1
    
    # calculate the number of good pairs using combinations formula
    for i in hashmap.values():
        count = count + (i * (i-1)) // 2

    return count 

    

# Test Case 1
input_1 = [1,2,3,1,1,3]
expected_output_1 = 4

# Test Case 2
input_2 = [1,1,1,1]
expected_output_2 = 6

# Test Case 3
input_3 = [1,2,3]
expected_output_3 = 0

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))