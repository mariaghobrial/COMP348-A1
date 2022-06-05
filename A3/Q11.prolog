lucasSeq(0, 2).
lucasSeq(1, 1).
lucasSeq(N, R) :- N > 1, N_Pre is N - 1, N_PrePre is N - 2, lucasSeq(N_Pre, LHS), lucasSeq(N_PrePre, RHS), R is LHS + RHS.

%numlist (first, end, return)
%maplist(function, parameter1, parameter2)
helper(NUM, Result) :- END is NUM -1, numlist(0, END, List), maplist(lucasSeq, List, Result).

%helper(2,R).
