# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    longestCommonPrefix = ""
    
    # sort the strings according to the length in ASC
    strs = sorted(strs, key=len)

    # iterate through the strings
    for i in range(len(strs[0])):
        # check if all the strings have the same character at the same index
        if(all(strs[0][i] == strs[j][i] for j in range(len(strs)))):
            longestCommonPrefix = longestCommonPrefix + strs[0][i]
        else:
            break
    print(longestCommonPrefix)

longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])