from collections import Counter
import heapq

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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        bucket = []
        for _ in range(len(words)):
            bucket.append(Trie())
        for word in words:
            trie = bucket[counter[word]]
            trie.insert(word)
        
        ans = []
        def printer(node, yet):
            if len(ans)==k:
                return
            if node.isEnd:
                ans.append(yet)
            if node.children == []:
                return
            for n in node.children:
                if n:
                    printer(n, yet+n.val)
            
        i = len(bucket)-1
        while len(ans)<k and i>-1:
            trie = bucket[i]
            printer(trie.root, '')
            i-=1
        
        return ans
#         counts = Counter(nums)
#         mapper = {}
#         for num, count in counts.items():
#             if count in mapper:
#                 mapper[count].append(num)
#             else:
#                 mapper[count] = [num]
                
#         for count, nums in mapper.items():
#             nums.sort()
#         minHeap = []
#         heapq.heapify(minHeap)

#         for count, nums in mapper.items():
#             for i in range(len(nums)):
#                 if len(minHeap) == k:
#                     if minHeap[0] < counts[nums[i]]:
#                         heapq.heappop(minHeap)
#                         heapq.heappush(minHeap, count)

#                 else:
#                     heapq.heappush(minHeap, count)

#         ans = []
#         minHeap = list(set(minHeap))
#         minHeap.sort(reverse=True)
#         for i in range(len(minHeap)):
#             if len(ans)==k:
#                 break
#             for i in mapper[minHeap[i]]:
#                 if len(ans)==k:
#                     break
#                 ans.append(i)

#         return ans