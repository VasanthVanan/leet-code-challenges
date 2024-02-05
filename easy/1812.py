# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

def function(inputs):
    xaxis = "bdfh"
    yaxis = "2468"
    # check if the input is a valid coordinate by checking if the first and second character is in the xaxis or yaxis
    if((inputs[0] in xaxis and inputs[1] not in yaxis) or (inputs[0] not in xaxis and inputs[1] in yaxis)):
        return True
    
    return False
# Test Case 1
input_1 = "a1"
expected_output_1 = False

# Test Case 2
input_2 = "h3"
expected_output_2 = True

# Test Case 3
input_3 = "c7"
expected_output_3 = False

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("\033[92m\nAll test cases passed!\n\033[0m")
except AssertionError as e:
    print("\033[91m\nError: {}\033[0m".format(e))