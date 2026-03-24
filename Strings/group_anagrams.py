# Problem: Group Anagrams (https://leetcode.com/problems/group-anagrams/description/)

# Problem statement:
# Given an array of strings strs, group the anagrams together. you can return the answer in any order

#pattern: Hashmap + freq counting(defaultdict)

#brute force idea
#create a list of groups
#for each word in strs, check all existing groups
# if sorted(word) equal to sorted(group[0]) first word of group -> add to that group
# if nothing matches, create another group with word

#brute force code
def group_anagrams(strs):
    groups = []
    for word in strs:
        placed = False
        for group in groups:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                placed = True
                break
        if not placed:
            groups.append([word])
    return groups


# Time: O(n^2 *k log k) - nested loops-O(n^2), sorting-O(k log k)   space: O(k) - stores in groups array

#why it's slow
# comparing every word or string with another string
# sorting takes k log k times
#slow for large input

#Optimized idea
# create a hashmap(deafultdict(list)) which automatically creates a list without creating it seperately
# for each word in strs -> sort the word -> use sorted word as key -> add words using key to group
# return all grouped lists

#Optimized code
from collections import defaultdict
def group_anagram(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

strs = ["eat","tea","act","ate","bat","bin","nib","cat"]
print(group_anagram(strs))


#Time: O(n * k log k) - sorting word takes -k log k
# Space:O(n*k) - storing all strings in hashmap/dict, sorting key value takes place