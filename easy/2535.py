# 2535. Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/ 

def function(inputs):
    elem_sum, dig_sum = 0, 0

    # Approach 1: Builtin functions
    # O(n) time complexity
    # elem_sum = sum(inputs)
    # convert the list to a string and then sum the digits
    # dig_sum = sum(list(map(int,''.join(list(map(str,inputs))))))

    # Approach 2: 
    # O(n * m) time complexity
    for i in inputs:
        elem_sum += i
        # if the number is greater than 9, find digits and add them to the sum
        if i > 9:
            while i > 0:
                dig_sum += i % 10
                i = i // 10
        # else add the number to the sum
        else:
            dig_sum += i

    # return the absolute difference between the sums
    return abs(elem_sum - dig_sum)

# Test Case 1
input_1 = [1,15,6,3]
expected_output_1 = 9

# Test Case 2
input_2 = [1,2,3,4]
expected_output_2 = 0

# Test Case 3
input_3 = [1]
expected_output_3 = 0

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))