# 2194. Cells in a Range on an Excel Sheet
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/ 

def function(inputs):
    # calculate distance between the first, last rows and columns
    diff1 = ord(inputs[3]) - ord(inputs[0]) + 1
    diff2 = int(inputs[-1]) - int(inputs[1]) + 1

    result = []

    # O(n)^2 time complexity
    for i in range(diff1):
        for j in range(diff2):
            # calculate its respective cell coordinate with 'i' and 'j'
            result.append("{}{}".format(chr(ord(inputs[0]) + i), int(inputs[1]) + j))

    return result

# Test Case 1
input_1 = "K1:L2"
expected_output_1 = ["K1","K2","L1","L2"]

# Test Case 2
input_2 = "A1:F1"
expected_output_2 = ["A1","B1","C1","D1","E1","F1"]

# Test Case 3
input_3 = "A2:D5"
expected_output_3 = ["A2","A3","A4","A5","B2","B3","B4","B5","C2","C3","C4","C5", "D2","D3","D4","D5"]

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("\033[92m All test cases passed!\033[0m")
except AssertionError as e:
    print("\033[91m Error: {}\033[0m".format(e))