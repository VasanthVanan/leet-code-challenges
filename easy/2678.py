# 2678. Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/description/

def function(inputs):
    def checkAge(detail):
        # check if the age is greater than 60 and if the gender is M or F or O
        if ('M' in detail or 'F' in detail or 'O' in detail):
            if(int(detail.split(detail[10])[-1][:2]) > 60):
                return True
            else:
                return False
    
    # iterate through the list and filter the number of senior citizens
    return len(list(filter(lambda x: checkAge(x), inputs)))

# Test Case 1
input_1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
expected_output_1 = 2

# Test Case 2
input_2 = ["1313579440F2036","2921522980M5644"]
expected_output_2 = 0

# Test Case 3
input_3 = ["5612624052M0130","5378802576M6424","5447619845F0171","2941701174O9078"]
expected_output_3 = 2

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("All test cases passed!")
except AssertionError as e:
    print("Error: {}".format(e))