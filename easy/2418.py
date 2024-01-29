# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people/description/

def function(inputs):
    names, heights = inputs[0], inputs[1]
    # method 1: hashmap approach
    hashmap = dict(zip(heights, names))
    return [hashmap[i] for i in sorted(heights, reverse=True)]
    
    # method 2: lambda function
    # indexes = list(range(len(heights)))
    # indexes.sort(reverse=True, key=lambda x: heights[x])
    # return [names[i] for i in indexes]


# Test Case 1
input_1 = [["Mary","John","Emma"], [180,165,170]]
expected_output_1 = ["Mary","Emma","John"]

# Test Case 2
input_2 = [["Alice","Bob","Bob"], [155,185,150]]
expected_output_2 = ["Bob","Alice","Bob"]

# Test Case 3
# input_3 = []
# expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    #assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("All test cases passed!")
except AssertionError as e:
    print("Error: {}".format(e))