# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):

    sum = 0 # add up values
    compare = 1 # the last letter we compared to

    # create a dictionary of mapped letters : numbers
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}

    # reverse the string
    s = s[::-1]

    # iterate through the string
    for i in s:
        if(roman_dict[i] > compare or roman_dict[i] == compare):
            sum = sum + roman_dict[i]
            compare = roman_dict[i]
        if(roman_dict[i] < compare):
            sum = sum - roman_dict[i]
            compare = roman_dict[i]

    print(sum)

romanToInt('MCMXCIV')
romanToInt('III')
romanToInt('LVIII')