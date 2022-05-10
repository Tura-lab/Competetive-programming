class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=d=0
        for s in senate:
            if s == 'R':
                r+=1
            else:
                d+=1
              
        if r==0:
            return 'Dire'
        if d==0:
            return 'Radiant'
        
        senate = list(senate)
        kd=kr=0
        while True:
            # print(senate)
            for i in range(len(senate)):
                s = senate[i]
                if s=='R':
                    if kr>0:
                        senate[i]=0
                        kr-=1
                    else:
                        kd+=1
                        d-=1
                    if d==0:
                        return 'Radiant'
                if s=='D':
                    if kd>0:
                        kd-=1
                        senate[i] = 0
                    else:
                        kr+=1
                        r-=1
                    if r==0:
                        return 'Dire'

        