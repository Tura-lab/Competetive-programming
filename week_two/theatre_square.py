row,col,a = [int(n) for n in input('').split(' ')]

i=j=1


if col<=a:
    i=1
elif col%a == 0:
    i=col//a
else:
    i = (col//a) +1
    
if row<=a:
    j=1
elif row%a == 0:
    j=row//a
else:
    j = (row//a) +1

if a == 1:
    print(row*col)
else:
    print(i*j)
