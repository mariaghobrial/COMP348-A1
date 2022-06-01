class Q4:

    def __init__(self, *elts):
        self.elts= list(elts)
       # self.items=[]

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elts

    def addelts(self,lst,elt):
        addedelt = list(lst)
        addedelt.append(elt)
        addedelt.sort()
        # Making the format
       # result = '{'+str(lst)[1:-1] + '} + '+ str(elt) + ' = {'+ str(addedelt)[1:-1] +'}'
        return addedelt


    # def add1(self, val):
    #     # adds one occurrence of val from the multiset, if any
    #     self.elts.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        while self.elts.count(val) != 0:
              self.elts.remove(val)
        return self.elts

    def countOcc(self,val):
         if self.elts.count(val) != 0:
             print("the number of occurences of",val,"is ", self.elts.count(val))
         else:
             print("The value is not in the list")

    def union(self, s1, s2):
        newLst=[]
        lst = list(set(s1).union(set(s2)))
        for i in set(lst):
            if i in s1 and i in s2: #if i is in both lists, then append it based on the max
                count_set1 = s1.count(i)
                count_set2 = s2.count(i)
                for j in range(max([count_set1, count_set2])):
                    newLst.append(i)
            elif i in s1 and i not in s2: #if i is in s1 only, then append it to lst
                 for j in range(s1.count(i)):
                    newLst.append(i)

            elif i not in s1 and i in s2: #if i is in s2 only, then append it to lst
                for j in range(s2.count(i)):
                  newLst.append(i)

        return newLst


    def intersec (self,s1,s2):
        newLst = []
        lst = list(set(s1).intersection(set(s2)))
        for i in set(lst):
            if i in s1 and i in s2: #if i is in both lists, then append it based on the max
                count_set1 = s1.count(i)
                count_set2 = s2.count(i)
                for j in range(min([count_set1, count_set2])):
                    newLst.append(i)
            elif i not in s1 and i not in s2:
                print("No common intersection")

        return newLst

    def Difference_Update(self , Set_A , Set_B):
        new_list = []
        for ele in set(Set_A):
            if ele not in Set_B:
                for j in range(Set_A.count(ele)):
                  new_list.append(ele)
            else:
               a_b = Set_A.count(ele) - Set_B.count(ele)
               for i in range(a_b):
                  new_list.append(ele)
        # Making the format
       # result = '{' + str(Set_A)[1:-1] + '} - {' + str(Set_B)[1:-1] +'} = {' + str(new_list)[1:-1] + '}'
        return new_list

    def diff(self,s1,s2):
        newLst = []
        for i in set(s1):
            if i not in s2:
                for j in range(s1.count(i)):
                    newLst.append(i)
            else:
               diffr = s1.count(i) - s2.count(i)
               for k in range(diffr):
                  newLst.append(i)
        return newLst













if __name__ == '__main__':

     test=Q4()
     print ("test add method ",test.addelts([1,3,4,9,9,9],9))
     print ("test remove method ",test.remove(9))

     print("test union method ",test.union([1,2], [2,2,3]))
     print ("test intersection ", test.intersec([1,2,3,4], [5,6,7]))

     print ("test difference_up ", test.Difference_Update([1,1,1,2,2,3],[1,2,2,2]))
   #  print ("test difference_up ", test.Difference_Update([10,20,30,40,80],[100,30,80,40,60]))

     print ("test diff ", test.diff([1,1,1,2,2,3],[1,2,2,2]))
   #  print ("test diff ", test.diff([10,20,30,40,80],[100,30,80,40,60]))

     #set=Q4(1,3,4,9,9,9) #union breaks cuz Q4 is initialized
    # set=Q4()
    # print("set remove method ",set.remove(9))
    # print("set union method ",set.union([1,2], [2,2,3]))
     #print("set add method",set.addelts([1,3,4,9,9,9],5))

   #  set2= Q4()
   #  set2.add1(3)
   #  print(set)
   # # set.add1(8)
   #  print(set)

   #  #print (set)
   #  set.countOcc(9)
   #  set.union(set,set2)
   #
   #  print(set)

    # set1={1, 2, 3}
    # sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
    # print(set1)
    # set1.add1(set1, 5)
    #  set1.add(5)
    # set1.__add__(5)
    # print(set1)


