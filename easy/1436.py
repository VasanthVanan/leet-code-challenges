# 1436. Destination City
# https://leetcode.com/problems/destination-city/description/ 

def function(inputs):
    visited = set()
    
    for i, j in inputs:
        # add the 'source' city to the set of visited cities
        visited.add(i)

    for i, j in inputs:
        # if the destination city is not in the set of 'source' visited cities, then return it
        if j not in visited:
            return j

# Test Case 1
input_1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
expected_output_1 = "Sao Paulo"

# Test Case 2
input_2 = [["B","C"],["D","B"],["C","A"]]
expected_output_2 = 'A'

# Test Case 3
input_3 = [["A","Z"]]
expected_output_3 = 'Z'

# Test Case 4
input_4 = [["A","B"],["C","D"],["B","E"],["E","C"],["D","F"]]
expected_output_4 = 'F'

# Test Case 5
input_5 = [["A","B"],["C","A"],["D","E"],["F","G"],["G","C"],["E","F"]]
expected_output_5 = 'B'

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    assert function(input_4) == expected_output_4, f"Test Case 4 Failed"
    assert function(input_5) == expected_output_5, f"Test Case 5 Failed"
    print("\033[92m\nAll test cases passed!\n\033[0m")
except AssertionError as e:
    print("\033[91m\nError: {}\033[0m".format(e))