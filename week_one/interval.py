def merge(self, interval):
    new_list = []
    interval = sorted(interval)
    current = interval[0]
    for i in range(len(interval)-1):
        if current[-1] >= interval[i+1][0]:
            current = [current[0], max(interval[i+1][-1], current[-1])]
        else:
            new_list.append(current)
            current = interval[i+1]
    new_list.append(current)

    return new_list
