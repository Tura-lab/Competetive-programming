class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        names = {
            '0': ['', '', 'Ten', ''],
            '1': ['One', '', 'Eleven', 'Thousand'],
            '2': ['Two', 'Twenty', 'Twelve', 'Million'],
            '3': ['Three', 'Thirty', 'Thirteen', 'Billion'],
            '4': ['Four', 'Forty', 'Fourteen'],
            '5': ['Five','Fifty', 'Fifteen'],
            '6': ['Six', 'Sixty', 'Sixteen'],
            '7': ['Seven', 'Seventy', 'Seventeen'],
            '8': ['Eight', 'Eighty', 'Eighteen'],
            '9': ['Nine', 'Ninety','Nineteen'],
        }
        ans = []
        i=0
        num = str(num)
        while i < len(num):
            if num[i] == '0':
                i+=1
                continue
            if len(num[i+1:])%3==0:
                ans.append(names[num[i]][0])
                ans.append(names[str(len(num[i:])//3)][3])
                i+=1
            elif len(num[i:])%3==2:
                if '1' == num[i]:
                    ans.append(names[num[i+1]][2])
                    ans.append(names[str(len(num[i+2:])//3)][3])
                    i+=2
                else:
                    ans.append(names[num[i]][1])
                    ans.append(names[num[i+1]][0])
                    ans.append(names[str(len(num[i+2:])//3)][3])
                    i+=2
            elif len(num[i:])%3 == 0:
                ans.append(names[num[i]][0])
                ans.append('Hundred')
                if num[i+1] =='0' and num[i+2]=='0':
                    ans.append(names[str(len(num[i+1:])//3)][3])
                i+=1
            
        
        return ' '.join([n for n in ans if n !=''])