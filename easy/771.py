# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

def function(inputs):
    a, b = inputs[0], inputs[1]
    # iterate through the string and count the number of jewels by using set and intersection
    return sum(1 for c in b if c in (set(a) & set(b)))
    


# Test Case 1
input_1 = ["aA","aAAbbbb"] 
expected_output_1 = 3
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = ["z", "ZZ"]
expected_output_2 = 0
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

print("All test cases passed!")