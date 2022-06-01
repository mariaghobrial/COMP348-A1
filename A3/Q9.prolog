sublist(_,0,0,[]). 
sublist([H | T], 0, END, [H | T2]):- END2 is END-1, sublist(T,0,END2,T2).
sublist([_ | T], START, END, O):- START2 is START-1, sublist(T, START2,  END, O).

?-sublist([1,2,3,4], 1, 2, O).
?-sublist([1,2,3,4], 0, 0, O).
?-sublist([1,2,3,4], 0, 10, O).
