class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        num_students = len(score)
        num_exams = len(score[0])
        
        scores_at_k = {i: score[i][k] for i in range(num_students)}
        

        return [score for i,score in sorted(list(enumerate(score)), reverse=True, key=lambda x: scores_at_k[x[0]])]