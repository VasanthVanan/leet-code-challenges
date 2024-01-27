# 2810. Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/description/ 

def function(inputs):
    count = inputs.count('i')
    final = inputs
    for i in range(count):
        # partition the string till 'i'
        partitioned = final.partition('i')
        final = (''.join([partitioned[0][::-1], partitioned[-1]]))
    return final


# Test Case 1
input_1 = "string"
expected_output_1 = "rtsng"
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = "poiinter"
expected_output_2 = "ponter"
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
input_3 = "minimalism"
expected_output_3 = "lammnsm"
assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

# Test Case 4
input_4 = "viwif"
expected_output_4 = "wvf"
assert function(input_4) == expected_output_4, f"Test Case 4 Failed"

print("All test cases passed!")