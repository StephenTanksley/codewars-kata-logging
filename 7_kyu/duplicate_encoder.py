"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""

from collections import Counter


def duplicate_encode(word):
    encoded_string = ""
    char_count = Counter(word.lower())

    for i in word.lower():
        if char_count[i] > 1:
            encoded_string += ")"
        else:
            encoded_string += "("

    print(encoded_string)
    return encoded_string


# Someone else's solution which is super slick. This implementation takes more time than mine does because it's an O(n ^ 2) implementation due to the use of the .count() method (O(n)) used inside another O(n) loop whereas mine is only O(n) due to the separation of the loops. My implementation trades space for time. --->

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
