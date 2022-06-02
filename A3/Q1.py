class Q1:

    

   #this fct returns the lucas seq
    def lucas1(self,n):
        luc=[2,1]
        for i in range(2, n+1):
            luc.append(luc[-1]+luc[-2])
        return luc
   
    #this fct prints all the number in the seq less than n
    def lu(self, n):
        lst = self.lucas1(n)
        lastelt = int(lst[len(lst)-1])

        while lastelt > n:
            lst.pop()
            lastelt = int(lst[len(lst)-1]) #need to update the value of lastelt
            if lastelt < n:
                pass
    
        return lst


if __name__ == '__main__':

     test=Q1()
     print(test.lucas1(5))
     print (test.lu(50))

