def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        closest = (grades[i]//5 +1)*5
        
        if abs(closest - grades[i]) >2:
            continue
        else:
            grades[i] = closest
    return grades
