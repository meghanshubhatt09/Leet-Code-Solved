class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}        
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in anagram_dict:
                anagram_dict[key].append(strs[i])
            else:
                anagram_dict[key] = [strs[i]]
        result = []
        for i in anagram_dict:
            result.append(anagram_dict[i])
        return result

        
        