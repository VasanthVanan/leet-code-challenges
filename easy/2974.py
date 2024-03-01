# 2974. Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/description/ 

def function(inputs):

    # sort the list
    nums = sorted(inputs)
    arr = []

    for i in range(0,len(nums),2):
        # extend the second and first element of the list
        arr.extend([nums[i+1], nums[i]])

    return arr

# Test Case 1
input_1 = [5,4,2,3]
expected_output_1 = [3,2,5,4]

# Test Case 2
input_2 = [2,5]
expected_output_2 = [5,2]

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