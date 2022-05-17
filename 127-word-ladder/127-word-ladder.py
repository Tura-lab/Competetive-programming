[0, 1, 1,1,1,2,2,2,2,3]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_graph = {}
        wordList = set(wordList)
        word_graph[beginWord] = []
        for word in wordList:
            word_graph[word] = []
        
        for i in range(len(beginWord)):
            for j in range(ord('a'), ord('z')+1):
                temp = beginWord[:i] + chr(j) + beginWord[i+1:]
                if temp in wordList and temp != beginWord:
                    word_graph[beginWord].append(temp)
        
        for word in wordList:
            for i in range(len(word)):
                for j in range(ord('a'), ord('z')+1):
                    temp = word[:i] + chr(j) + word[i+1:]
                    if temp in wordList and temp!=word:
                        word_graph[word].append(temp)
        
        # print(word_graph)
        # return
        distances = {}
        for word in wordList:
            distances[word] = -1

        distances[beginWord] = -1
        q = collections.deque()
        q.append(beginWord)
        
        i=1
        while q:
            n = len(q)
            for _ in range(n):
                word=q.popleft()
                if distances[word] == -1:
                    if word == endWord:
                        return i
                    distances[word] = i
                
                    for w in word_graph[word]:
                        q.append(w)
            i+=1
            
                
        return 0
            