class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        stn = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        nts = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

        p,x = 0,0
        for char in reversed(num1):
            v = stn[char]
            x += (v * (10**p))
            p += 1
        
        
        p,y = 0,0
        for char in reversed(num2):
            v = stn[char]
            y += (v * (10**p))
            p += 1

        res = x*y
        if res == 0: return '0'
        sres = ""
        while res > 0:
            rem = res % 10
            res = res // 10
            sres = nts[rem] + sres
        
        return sres



        
