class TrieNode:
    def __init__(self, val=None):
        self.children = {}
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
            node.score += 1 

    def search(self, word: str) -> bool:
        node = self.root
        tot = 0
        for c in word:
            node = node.children[c]
            tot += node.score
        
        return tot

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return [trie.search(word) for word in words]









# class Solution:
#     def sumPrefixScores(self, words: List[str]) -> List[int]:
#         '''
#         ['b', 'ab', 'bc', 'abc']
#         '''
#         print(len(words), len(words[0]))
#         score = defaultdict(int)
        
#         def h(c):
#             return ord(c)-ord('a') + 1
        
#         # words.sort(key=lambda x: len(x))
        
#         for j in range(len(words)):
#             word = words[j]
#             p = 1
#             hash = 0
            
#             for i in range(len(word)):
#                 p *= 26
#                 hash += p*h(word[i])
#                 score[hash] += 1

#         ans = []
#         for i in range(len(words)):
#             word = words[i]
#             count = 0
#             p=1
#             hash = 0
#             for j in range(len(word)):
#                 p*=26
#                 hash += p*h(word[j])
#                 count += score[hash]
                
#             ans.append(count)
            
#         return ans