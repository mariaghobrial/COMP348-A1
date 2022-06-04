lucasSeq(0, 2).
lucasSeq(1, 1).
lucasSeq(N, R) :- N > 1, N_Pre is N - 1, N_PrePre is N - 2, lucasSeq(N_Pre, LHS), lucasSeq(N_PrePre, RHS), R is LHS + RHS.

helper(M, Result) :- numlist(0, M, List), maplist(lucasSeq, List, Result).

helper(2,R).
