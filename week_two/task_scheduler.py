class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        count_dict = {}
        for task in tasks:
            if task not in count_dict:
                count_dict[task]=1
            else:
                count_dict[task]+=1
        count_dict = sorted( count_dict.items(), key = lambda task: task[-1], reverse=True )
        print(count_dict)
        mx = count_dict[0][-1]
        mx_count=1
        for i in range(1,len(count_dict)):
            if count_dict[i][-1] == mx:
                mx_count+=1
        least = mx + (mx-1)*n + (mx_count-1)
        free_spaces = least - (mx * mx_count)
        rem_tasks = len(tasks)-(mx*mx_count)
        if rem_tasks  <= free_spaces:
            return least
        return least + (rem_tasks - free_spaces)
