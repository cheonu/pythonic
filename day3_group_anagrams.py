# Day 3: Group Anagrams
#
# Given a list of strings, group the ones that are anagrams of each other.
# Two words are anagrams if they contain the exact same letters 
# in a different order (e.g., "eat" and "tea").
#
# Example:
#   Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
#   Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# Notes:
#   - The order of groups and order within groups doesn't matter
#   - All inputs will be lowercase letters
#
# Hint: What property do all anagrams share? How could you use that 
#       as a dictionary key?
#
# Write your solution below:

def group_anagrams(strs):
    groups = {}
    
    for s in strs:
        key = "".join(sorted(s))
        
        if key not in groups:
            groups[key] = []
        
        groups[key].append(s.lower())

    return list(groups.values())

# Test cases
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(group_anagrams([""]))
# Expected: [[""]]

print(group_anagrams(["a"]))
# Expected: [["a"]]
