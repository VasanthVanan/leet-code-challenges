# 1309. Decrypt String from Alphabet to Integer Mapping
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/ 

def function(inputs):
    strings = ""
    index = 0
    while index < len(inputs):
        # if the character is a digit, add the corresponding ASCII character to the string
        if inputs[index].isdigit():
            if index+2 < len(inputs) and inputs[index+2] == "#":
                strings += chr(int(inputs[index:index+2]) + 96)
                index += 2
            else:
                strings += chr(int(inputs[index]) + 96)
                index += 1
        else:
            index += 1
    return strings


# Test Case 1
input_1 = "10#11#12"
expected_output_1 = "jkab"

# Test Case 2
input_2 = "1326#"
expected_output_2 = "acz"

# Test Case 3
# input_3 = []
# expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    # assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("All test cases passed!")
except AssertionError as e:
    print("Error: {}".format(e))