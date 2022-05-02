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
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def dfs(node, yet):
            if len(found)==3:
                return
            if node.isEnd:
                found.append(yet+node.val)
            for n in node.children:
                d=0
                if n and node.val:
                    dfs(n, yet+node.val)
                    
        trie = Trie()
        ans = []
        for product in products:
            trie.insert(product)
            
        for i in range(len(searchWord)):
            d=0
            w = searchWord[:i]
            node = trie.root
            for j in range(i+1):
                c = searchWord[j]
                if node.children[ord(c)-ord('a')]:
                    node = node.children[ord(c)-ord('a')]
                else:
                    d=1
                    break
            
            
            found = []
            if d==0:
                dfs(node, w)
            ans.append(found)
            
        return ans                 