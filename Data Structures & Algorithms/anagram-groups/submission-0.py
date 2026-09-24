class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # need to go through each word and count occurences of letter
        # then need to match all of words w same letter rate w/each other
        # return these all in a list, in any order
        anagram_list = {}
        for string in strs:
            letters = list(string)
            letters.sort()
            letters = tuple(letters)
            if letters not in anagram_list:
                anagram_list[letters] = [string]
            else:
                anagram_list[letters].append(string)
        return list(anagram_list.values())
            