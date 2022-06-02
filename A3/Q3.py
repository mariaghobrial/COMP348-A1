class Q3:
    def customSet(self, seq):

        lengthSeq = len(seq)
        if lengthSeq == 0:
            return []
        # u = {} #initialize empty dict
        # try:
        #     for x in seq:
        #         u[x] = 1
        # except TypeError:
        #     del u  # Move on to the next method
        # else:
        #     return u.keys()
        try:
            t = list(seq)
            t.sort()
        except TypeError:
            del t
        else:
            assert lengthSeq > 0
            last = t[0]
            lasti = i = 1
            while i < lengthSeq:
                if t[i] != last:
                    t[lasti] = last = t[i]
                    lasti += 1
                i += 1
            return t[:lasti]

        u = []
        for x in seq:
            if x not in u:
                u.append(x)
        return u

if __name__ == '__main__':

    test=Q3()
    print(test.customSet([1, 2, 3, 1, 2, 3]))
    print(test.customSet("abcabc"))
    print(test.customSet(([1, 2], [2, 3], [1, 2])))


