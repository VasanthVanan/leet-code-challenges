# 2824. Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/ 

def function(inputs):
    nums, target = inputs[0], inputs[1]
    count = 0
    # O(n)^2 Complexity
    # for i in range(len(nums)-1):
    #     for j in range(i,len(nums)):
    #         if i != j and (nums[i] + nums[j]) < target:
    #             count += 1

    nums.sort()
    start, end = 0, len(nums)-1
    # O(n) time complexity
    while start < end:
        # compare the sum of two numbers with the target
        if nums[start] + nums[end] < target:
            # count the number of pairs whose sum is less than target
            count += end - start
            # move the pointer to the right
            start += 1
        else:
            # move the pointer to the left
            end -= 1
        #print("Count:{} Start:{} End:{} Accessed: {},{}".format(count, start, end, nums[start], nums[end]))
    return count

# Test Case 1
input_1 = [[-1,1,2,3,1],2]
expected_output_1 = 3

# Test Case 2
input_2 = [[-6,2,5,-2,-7,-1,3],-2]
expected_output_2 = 10

# Test Case 3
input_3 = [[1,3],-1]
expected_output_3 = 0

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))