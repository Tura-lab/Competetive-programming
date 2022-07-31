class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = defaultdict(list)
        
        for word in strs:
            found[''.join(sorted(word))].append(word)
        
        return found.values()