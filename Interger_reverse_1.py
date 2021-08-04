class Solution(object):
    def reverse(self,x):
        #check the lower and higher limit
        if x > pow(2,31) or x < pow(2,-31):
            return 0
        else:
            #Convert to string
            x = str(x)
            #do string reversal using 
            for i in x:
                #convert the string to integer
                return int(x[::-1])
                

t =  Solution()
print(t.reverse(=213)