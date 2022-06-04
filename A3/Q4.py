class Q4:
    #default constructor
    def __init__(self, *elts):
        self.elts= list(elts)
       # self.items=[]

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elts

    #method to add elts to the set
    def addelts(self, lst, elt):
        addedelt = list(lst) #make the added elt as a lst
        addedelt.append(elt) #append the added elt to the lst
        addedelt.sort() #sorts the final lst
        # Making the format
       # result = '{'+str(lst)[1:-1] + '} + '+ str(elt) + ' = {'+ str(addedelt)[1:-1] +'}'
        return addedelt

    def removeAll(self, lst, val):
        if lst.count(val) == 0:
            print("elt not found")

        for i in lst:
            if lst.count(val) != 0:
                lst.remove(val)

        return lst

    def countOcc(self, lst, val):
         if lst.count(val) == 0:
            print("The value is not in the list")

         if lst.count(val) != 0:
             return print("the number of occurences of",val,"is ", lst.count(val))

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

    def intersec (self, s1, s2):
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
     #-------------TESTING ADD ELTS METHOD-------------------#
     print("test add method ", test.addelts([1, 3, 4, 9, 9, 9], 9))

    #-------------TESTING REMOVE METHOD-------------------#
     print("test remove method ", test.removeAll([1, 3, 4, 9, 9, 9], 9))

    #-------------TESTING COUNT OCCURENCES METHOD-------------------#
     test.countOcc([1, 3, 4, 9, 9, 9], 9)

     #-------------TESTING UNION  METHOD-------------------#
     print("test union method ", test.union([1, 2], [2, 2, 3]))

    #-------------TESTING INTERSECTION METHOD-------------------#
     print ("test intersection ", test.intersec([1, 1, 2, 2, 3], [2, 2, 2, 3, 4]))

      #-------------TESTING DIFFERENCE METHOD-------------------#

     print("test diff ", test.diff([1, 1, 1, 2, 2, 3], [1, 2, 2, 2]))
     print("test diff ", test.diff([10, 20, 30, 40, 80], [100, 30, 80, 40, 60]))




