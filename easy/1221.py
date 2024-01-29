# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

def function(inputs):
    # code goes here
    counter = 0
    balanced = 0
    for current in inputs:
        # if the counter is 0, then we have a balanced string
        if(current == 'L'):
            counter += 1
        if(current == 'R'):
            counter -= 1
        if(counter == 0):
            balanced += 1

    return balanced


# Test Case 1
input_1 = "RLRRLLRLRL" 
expected_output_1 = 4

# Test Case 2
input_2 = "RLRRRLLRLL"
expected_output_2 = 2

# Test Case 3
input_3 = "LLLLRRRR"
expected_output_3 = 1

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("All test cases passed!")
except AssertionError as e:
    print("Error: {}".format(e))

