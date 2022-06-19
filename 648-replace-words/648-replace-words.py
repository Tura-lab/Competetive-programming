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
    
    def traverse(self, prefix):
        node = self.root
        j=0
        for i in range(len(prefix)):
            c = prefix[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return j if node.isEnd else 0
            
            if node.isEnd:
                return j;
            
            node = node.children[ord(c) - ord('a')]
            j+=1
        
        return j


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        s = sentence.split()
        for i in range(len(s)):
            word = s[i]
            ans = trie.traverse(word)
            if ans !=0:
                s[i] = s[i][:ans]
            
        return ' '.join(s)
                    
                
        
        
        
        