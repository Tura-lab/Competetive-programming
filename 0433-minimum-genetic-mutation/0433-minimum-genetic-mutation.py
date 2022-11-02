class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([start])
        visited = set([start])
        bank = set(bank)
        count = 0
        
        def check(a,b):
            dif=0
            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    dif += 1
                if dif == 2:
                    return False    
            return True
        
        
        while q:
            for _ in range(len(q)):
                cur_gene = q.popleft()
                
                if cur_gene == end:
                    return count
                
                for gene in bank:
                    if gene not in visited and check(gene, cur_gene):
                        visited.add(gene)
                        q.append(gene)
                    
            count += 1
        
        return -1