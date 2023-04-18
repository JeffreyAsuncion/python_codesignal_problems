"""
557. Reverse Words in a String III
Easy
4.3K
214
company
Facebook
company
Amazon
company
Apple
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

def reverseWords(s: str) -> str:
    words = s.split(" ")
    length = len(words)
    answer = ""
    for i in range(length):
        words[i] = words[i][::-1]
        answer += words[i] + ' '
    return answer[:-1]

# Input: 
s = "God Ding"
# Output: "doG gniD"
print(reverseWords(s))