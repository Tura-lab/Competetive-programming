class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==1:
            return n==0
        elif len(flowerbed)==1:
            return n<2
        if len(flowerbed)==2 and flowerbed[0]==flowerbed[1]==0:
            return n<2
        elif len(flowerbed)==2:
            return n==0
    
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            elif i==len(flowerbed)-1 and flowerbed[i-1]==flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
            elif flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            if n<=0:
                return True
        
        return False
            