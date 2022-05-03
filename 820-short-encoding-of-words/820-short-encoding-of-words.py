class TrieNode:
    def __init__(self, val=None):
        self.val = val 
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if node.children[ord(c)-ord('a')] == None:
                n = TrieNode(val=c)
                node.children[ord(c)-ord('a')] = n
            node = node.children[ord(c)-ord('a')]
        node.isEnd=True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def ok(word):
            for i in range(len(word)):
                if word[i:] in seen:
                    seen.remove(word[i:])
                    seen.add(word)
                    return False
            return True
        words.sort(key=lambda x:len(x))
        
#         trie = Trie()
#         for word in word:
#             trie.insert(word)
            
        seen = set()
        
        for word in words:
            if ok(word):
                seen.add(word)
        
        ans = 0
        for word in seen:
            ans += len(word) +1
        
        return ans
                