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

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return False
            node = node.children[ord(c) - ord('a')]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return False
            node = node.children[ord(c) - ord('a')]
        
        return True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
            
        ans = []
        for word in sentence.split():
            node = trie.root
        
            i=0
            f=0
            while not node.isEnd and i<len(word):
                c = word[i]
                if node.children[ord(c)-ord('a')]:
                    node = node.children[ord(c)-ord('a')]
                else:
                    f=1
                    break
                i+=1
            if node.isEnd and not f:
                ans.append(word[:i])
            else:
                ans.append(word)
        
        
        return ' '.join(ans)