# 1534. Count Good Triplets
# https://leetcode.com/problems/count-good-triplets/description/ 

def function(inputs):
    nums, a, b , c = inputs[0], inputs[1], inputs[2], inputs[3]
    # O(n^3) time complexity
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            # checks the condition: |arr[i] - arr[j]| <= a
            if(abs(nums[i] - nums[j]) <= a):
                for k in range(j+1,len(nums)):
                    # checks conditions: |arr[j] - arr[k]| <= b, |arr[i] - arr[k]| <= c
                    if(abs(nums[j] - nums[k]) <= b and abs(nums[i] - nums[k]) <= c):
                        # if all conditions are met, increment the count
                        count += 1
    return count

# Test Case 1
input_1 = [[3,0,1,1,9,7],7,2,3]
expected_output_1 = 4

# Test Case 2
input_2 = [[1,1,2,2,3],0,0,1]
expected_output_2 = 0

# Test Case 3
input_3 = [[7,3,7,3,12,1,12,2,3], 5,8,1]
expected_output_3 = 12

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))