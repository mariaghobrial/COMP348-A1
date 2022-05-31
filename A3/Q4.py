class Q4:

    def __init__(self, *elts):
        self.elts= list(elts)
       # self.items=[]

    # def __repr__(self):
    #     return " " %self.elts
    #
    # def __str__(self):
    #     return " " %self.elts

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elts


    def add1(self, val):
        # adds one occurrence of val from the multiset, if any
        self.elts.append(val)
    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        while self.elts.count(val) != 0:
              self.elts.remove(val)

    def countOcc(self,val):
         if self.elts.count(val) != 0:
             print("the number of occurences of",val,"is ", self.elts.count(val))
         else:
             print("The value is not in the list")

    def union (self, set1, set2):
        newLst=[]
        lst = list(set(set1).union(set(set2)))
        for i in set(lst):
            if i in set1 and i in set2:
                count_set1 = set1.count(i)
                count_set2 = set2.count(i)
                for j in range(max([count_set1, count_set2])):
                    newLst.append(i)
            elif i in set1 and i not in set2:
                 for j in range(set1.count(i)):
                    newLst.append(i)

            elif i not in set1 and i in set2:
                for j in range(set2.count(i)):
                  newLst.append(i)

        result = '{' + str(set1)[1:-1] + '} U {' + str(set2)[1:-1] +'} = {' + str(newLst)[1:-1] + '}'











        # def Union_with_another_set(self , Set_a , Set_b):
        #     new_list = []
        #     large_lst =list(set(Set_a).union(set(Set_b)))
        #     for i in set(large_lst):
        #     if i in Set_a and i in Set_b:
        #     count_a = Set_a.count(i)
        #     count_b = Set_b.count(i)
        #     for j in range(max([count_a , count_b])):
        #     new_list.append(i)
        #         elif i in Set_a and i not in Set_b:
                    # for j in range(Set_a.count(i)):
                    # new_list.append(i)
        #
        # elif i not in Set_a and i in Set_b:
        # for j in range(Set_b.count(i)):
        # new_list.append(i)
        # # Making the format
        # result = '{' + str(Set_a)[1:-1] + '} U {' + str(Set_b)[1:-1] +'} = {' + str(new_list)[1:-1] + '}'
        # return result










        # for val in set:
        #     if val in set:
        #         count +=1
        #     else:
        #         pass


         # while self.elts.count(val) != 0:
         #      self.elts.remove(val)


if __name__ == '__main__':
    set=Q4(1,3,4,9,9,9)
    set2= Q4()
    set2.add1(3)
    print(set)
   # set.add1(8)
    print(set)
   # set.remove(9)
    #print (set)
    set.countOcc(9)
    set.union(set,set2)

    print(set)





    # set1={1, 2, 3}
    # sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
    # print(set1)
    # set1.add1(set1, 5)
    #  set1.add(5)
    # set1.__add__(5)
    # print(set1)


