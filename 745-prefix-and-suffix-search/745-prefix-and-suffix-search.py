class TrieNode:
    def __init__(self, val=None):
        self.val = val 
        self.children = [None]*26
        self.isEnd = False
        self.indexA = []
        self.indexB = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx, a=1) -> None:
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if node.children[ord(c)-ord('a')] == None:
                n = TrieNode(val=c)
                node.children[ord(c)-ord('a')] = n
            node = node.children[ord(c)-ord('a')]
            if a==0:
                node.indexB.add(idx)
            else:    
                node.indexA.append(idx)
        node.isEnd=True
        
    def startsWith(self, prefix: str, a=1) -> bool:
        node = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if not node.children[ord(c) - ord('a')] or node.children[ord(c) - ord('a')].val != c:
                return -1
            node = node.children[ord(c) - ord('a')]
        
        return node.indexA if a==1 else node.indexB


class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_trie = Trie()
        self.post_trie = Trie()
        self.words = words
        
        for i in range(len(words)):
            word = words[i]
            self.pre_trie.insert(word, i)
        for i in range(len(words)):
            word = words[i]
            self.post_trie.insert(word[::-1], i, 0)

    def f(self, prefix: str, suffix: str) -> int:
        pre = self.pre_trie.startsWith(prefix)
        post = self.post_trie.startsWith(suffix[::-1],0)
        
        if pre==-1 or post == -1:
            # print(post)
            return -1
        
        # print(pre)
        # print(post)
        i=len(pre)-1
        while i>-1:
            if pre[i] in post:
                return pre[i]
            i-=1
        return -1
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)