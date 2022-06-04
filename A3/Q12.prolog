start(a).

final(a).
final(d).
final(f).

tran(a,0,b).
tran(a,1,c).
tran(b,0,a).
tran(b,1,d).
tran(c,0,f).
tran(c,1,e).
tran(d,0,f).
tran(d,1,e).
tran(e,0,e).
tran(e,1,e).
tran(f,0,f).
tran(f,1,e).

last(X,[],X).
last(X,[H|T],X2) :- tran(X,H,X1),last(X1,T,X2).

accepted(L) :- start(X),last(X,L,X1),final(X1),!.

?-accepted([1,0]).
?-accepted([0,1,0,1]).
