# Leet Code Challenges: Practice

This repository contains solutions to [Leet Code](https://leetcode.com/) easy challenges. Each solution is organised by its corresponding problem number. 

### Keyword Search

It will be easier to find a solution by entering a specific `KEYWORD` in the search bar.

```
https://github.com/VasanthVanan/leet-code-challenges/search?q=KEYWORD
```

Example: Parentheses <a href="https://github.com/VasanthVanan/leet-code-challenges/search?q=Parentheses" target="_blank">https://github.com/VasanthVanan/leet-code-challenges/search?q=Parentheses</a>

### Template Configuration

This repo uses a common `template.py` for most of the files. To reuse this template, you can configure it using VSCode.

1. Open the command palette by pressing Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac).
2. Select "Snippets: Configure User Snippets" from the dropdown
3. select "python" as the template language
4. Copy & paste the following snippet:
   <details>
     <summary>Leetcode: Python Template</summary>

   ```json
   {
        "Leetcode Template": {
            "prefix": "lc-temp",
            "body": [
                "# Title"
                "# URL "
                ""
                "def function(inputs):"
                ""
                "    return"
                ""
                "# Test Case 1"
                "input_1 = []"
                "expected_output_1 = []"
                ""
                "# Test Case 2"
                "input_2 = []"
                "expected_output_2 = []"
                ""
                "# Test Case 3"
                "input_3 = []"
                "expected_output_3 = []"
                ""
                "try:",
                "    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'",
                "    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'",
                "    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'",
                "    print('\\033[92m All test cases passed! \\033[0m')",
                "except AssertionError as e:",
                "    print('\\033[91m Error: {}\\033[0m'.format(e))"
            ],
            "description": "Leetcode Python Template"
        }
   }
   ```

   </details>
5. use this template in a new file by typing `lc-temp` and hitting enter.
