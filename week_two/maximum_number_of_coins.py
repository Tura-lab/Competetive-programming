def maxCoins(self, piles):
    piles = sorted(piles, reverse=True)
    new_arr = []
    j=len(piles)-1
    i=0
    while len(new_arr)<len(piles):
        new_arr.append(piles[i])
        new_arr.append(piles[i+1])
        new_arr.append(piles[j])
        i+=2
        j-=1
    mine = 0
    for i in range(2, len(new_arr), 3):
        mine += (new_arr[i-2:i+1])[1]
    return mine
