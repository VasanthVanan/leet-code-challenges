# 2315. Count Asterisks
# https://leetcode.com/problems/count-asterisks/description/

def function(inputs):
    # split the words
    splitted = inputs.split('|')
    counter = 0
    if(len(splitted)):
        # Method 1: Naive approach
        # return the sum of the asterisks in even indices using enumerate
        # for i,e in enumerate(splitted):
        #     if(i % 2 == 0):
        #         counter += e.count('*')
        # return counter

        # Method 2: Python Functions
        # return the sum of the asterisks in even indices using list comprehension
        return sum([e.count('*') for i,e in list(filter(lambda x: x[0] % 2 == 0, enumerate(splitted)))])

    else:
        return 0


# Test Case 1
input_1 = "l|*e*et|c**o|*de|" 
expected_output_1 = 2
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = "iamprogrammer"
expected_output_2 = 0
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
input_3 = "yo|uar|e**|b|e***au|tifu|l"
expected_output_3 = 5
assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

print("All test cases passed!")