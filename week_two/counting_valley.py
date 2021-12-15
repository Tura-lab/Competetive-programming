def countingValleys(steps, path):
    pos = 0
    valie_count = 0
    for step in path:
        if step == 'U':
            last_pos = pos
            pos+=1
        else:
            last_pos = pos
            pos-=1
        if pos<0 and last_pos >=0:
            valie_count+=1
    return valie_count
