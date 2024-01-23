# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/description/

def function(inputs):
    # create a hash map of morse code
    hash_map = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.", "o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    counter = 0
    list_words = set()

    # iterate through the words
    for w in inputs:
        w = ''.join(hash_map[c] for c in w.lower())
        # check if the word is already in the set
        if w not in list_words:
            list_words.add(w)
            counter += 1

    return counter


# Test Case 1
input_1 = ["gin","zen","gig","msg"]
expected_output_1 = 2
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = ["a"]
expected_output_2 = 1
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

print("All test cases passed!")