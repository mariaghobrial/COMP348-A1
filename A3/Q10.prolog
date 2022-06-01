every-other([],[]). 
every-other([H],[H]).
every-other([H,_ | T1], [H | T2]):-every-other(T1,T2).%_ is to skip the next element after the H

every-other([], O).
every-other([1], O).
every-other([1,2], O).
every-other([1,2,3], O).
every-other([1,2,3,4,], O).
