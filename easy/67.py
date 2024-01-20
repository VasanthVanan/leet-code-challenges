# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

def function(inputs):
    # convert the binary strings to integers
    a, b = int(inputs[0], 2), int(inputs[1], 2)
    sum = a + b
    return bin(sum)[2:]

# Test Case 1
input_1 = ["11","1"]
expected_output_1 = "100"
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = ["1010","1011"]
expected_output_2 = "10101"
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

print("All test cases passed!")