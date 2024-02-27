# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/description/

def function(inputs):
    s, indices = inputs[0], inputs[1]
    # mapping approach:
    hashmap = {}
    for i, x in enumerate(indices):
        hashmap[x] = s[i]
    return ''.join([hashmap[x] for x in range(len(s))])

# Test Case 1
input_1 = ["codeleet", [4,5,6,7,0,2,1,3]] 
expected_output_1 = "leetcode"

# Test Case 2
input_2 = ["abc", [0,1,2]]
expected_output_2 = "abc"

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