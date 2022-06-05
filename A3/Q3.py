class Q3:
    def custom_set(self, seq):
        lengthSeq = len(seq)
        if lengthSeq == 0:
            return []
        else:
            lst = list(seq)
            lst.sort()
           # assert lengthSeq > 0
            current = lst[0]
            new = i = 1
            #removing duplicates
            while i < lengthSeq:
                if lst[i] != current:
                    lst[new] = current = lst[i]
                    new += 1
                i += 1
            return lst[:new]
      


if __name__ == '__main__':

    test=Q3()
    print(test.custom_set([1, 2, 3, 1, 2, 3]))
    print(test.custom_set([ 3, 1, 2]))
    #print(test.custom_set("abcabc"))
    #print(test.custom_set(([1, 2], [2, 3], [1, 2])))


